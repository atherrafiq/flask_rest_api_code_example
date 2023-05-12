import http
import json
import openpyxl
from flask_restx import Namespace, Resource, fields
from werkzeug.utils import secure_filename
from flask_jwt_extended import jwt_required, get_jwt_identity, get_current_user
from ..models.auth_models import *
from ..models.tenders_models import *
from http import HTTPStatus
from ..utils.db import db
from flask import request
from decouple import config
import os, shutil

tenders_namespace = Namespace('tenders', description="Namespace for tenders")


@tenders_namespace.route('/createTender')
class createTender(Resource):

    @jwt_required()
    def post(self):
        """
            create a new tender
        """
        user_Id = get_jwt_identity()
        data = request.get_json()
        tenders = Tenders(**data)
        tenders.save()

        tenderLogs = TenderLogs(
            ten_Tender_Id=tenders.Id,
            FieldName='New Tender Created',
            UpdatedBy_Id=user_Id
        )
        tenderLogs.save()

        return 'Tender Added Successfully.', HTTPStatus.CREATED


@tenders_namespace.route('/updateTender')
class updateTender(Resource):

    @jwt_required()
    def post(self):
        """
            update a tender
        """
        user_Id = get_jwt_identity()
        data = request.get_json()

        Id = data['Id']
        del data['Id']

        lessonsLearned = data['LessonsLearned']
        del data['LessonsLearned']

        # tenders = Tenders.query.get(Id)
        tenders = Tenders.query.filter_by(Id=Id).first()
        for attribute, value in data.items():

            old_value = getattr(tenders, attribute)
            updated_value = value

            # save the logs for updated field
            if old_value != updated_value:
                tenderLogs = TenderLogs(
                    ten_Tender_Id=Id,
                    FieldName=attribute,
                    ValueBefore=old_value,
                    ValueAfter=updated_value,
                    UpdatedBy_Id=user_Id,
                )
                tenderLogs.save()

            # updating the attribute
            setattr(tenders, attribute, value)

        LessonsLearned.query.filter_by(ten_Tender_Id=Id).delete()
        for lesson in lessonsLearned:
            del lesson['Id']
            lessonslearned = LessonsLearned(**lesson)
            lessonslearned.save()

        db.session.commit()

        # updated_object = Tenders.query.filter_by(Id=Id).first()
        # updated_object = updated_object.serialize
        #
        # lessonsLearned = LessonsLearned.query.filter_by(ten_Tender_Id=Id).all()
        # updated_object['LessonsLearned'] = [x.serialize for x in lessonsLearned]

        return 'Tender Updated Successfully.', HTTPStatus.OK


@tenders_namespace.route('/getTendersList')
class getTendersList(Resource):

    @jwt_required()
    def get(self):
        """
            get all tenders
        """
        tenders = Tenders.query.order_by(Tenders.Id.desc()).all()

        natureOfWorks = NatureOfWorks.query.all()
        natureOfWorks = {x.Id: x.NatureOfWorkName for x in natureOfWorks}

        tenderStatus = TenderStatus.query.all()
        tenderStatus = {x.Id: x.TenderStatusName for x in tenderStatus}

        industry = Industry.query.all()
        industry = {x.Id: x.IndustryName for x in industry}

        country = Country.query.all()
        country = {x.Id: x.CountryName for x in country}

        response_data = []
        for x in tenders:
            x = x.serialize

            try:
                x['NatureOfWork_Id'] = natureOfWorks[x['NatureOfWork_Id']]
            except:
                x['NatureOfWork_Id'] = ''

            try:
                x['TenderStatus_Id'] = tenderStatus[x['TenderStatus_Id']]
            except:
                x['TenderStatus_Id'] = ''

            try:
                x['Industry_Id'] = industry[x['Industry_Id']]
            except:
                x['Industry_Id'] = ''

            try:
                x['Country_Id'] = country[x['Country_Id']]
            except:
                x['Country_Id'] = ''

            response_data.append(x)

        return response_data, HTTPStatus.OK


@tenders_namespace.route('/getTenderById')
class getTenderById(Resource):

    @jwt_required()
    def get(self):
        """
            get tender by Id
        """
        tender_id = request.args.get('tender_id')
        tender = Tenders.query.filter_by(Id=tender_id).first()

        if tender:
            response_data = tender.serialize
            response_data['LessonsLearned'] = [x.serialize for x in tender.lessonsLearned]
            response_data['TenderFinancialData'] = get_tender_financial_data(tender.tenderFinancialData)
            response_data['TenderEquipmentCost'] = [x.serialize for x in tender.tenderEquipmentCost]

            return response_data, HTTPStatus.OK

        return 'Not Found', HTTPStatus.NOT_FOUND


def get_tender_financial_data(tenderFinancialData):

    arranged_tenderFinancialData = []
    ten_EquipmentCostItemIds = [x.ten_EquipmentCostItemId for x in tenderFinancialData if x.ten_EquipmentCostItemId != 0]

    equipmentCostItem = EquipmentCostItem.query.filter(
        EquipmentCostItem.Id.in_(ten_EquipmentCostItemIds)
    ).order_by(
        EquipmentCostItem.Id
    ).all()

    equipmentCostItem = {x.Id: x.serialize for x in equipmentCostItem}

    rows_to_sum = []

    for financialData in tenderFinancialData:

        updated_row = financialData.serialize

        if financialData.ten_EquipmentCostItemId in equipmentCostItem:
            updated_row['AED'] = equipmentCostItem[financialData.ten_EquipmentCostItemId]['ItemReference']
            updated_row['Item'] = equipmentCostItem[financialData.ten_EquipmentCostItemId]['Item']
            updated_row['IsParent'] = equipmentCostItem[financialData.ten_EquipmentCostItemId]['ParentId']

        arranged_tenderFinancialData.append(updated_row)

        if updated_row['AED'] in ['A', 'B', 'C', 'D', 'E']:
            rows_to_sum.append(updated_row)


    arranged_tenderFinancialData = sorted(arranged_tenderFinancialData, key=lambda x: x['AED'])

    if len(rows_to_sum) > 0:
        total = {key: sum(e[key] for e in rows_to_sum if isinstance(e[key], int) or isinstance(e[key], float)) for key in rows_to_sum[0].keys()}
        total['AED'] = ''
        total['Item'] = 'Total'
        total['IsParent'] = False
        arranged_tenderFinancialData.append(total)

    return arranged_tenderFinancialData


@tenders_namespace.route('/uploadTenderFinancialData')
class uploadTenderFinancialData(Resource):

    @jwt_required()
    def post(self):
        """
            upload tender financial data - Excel file
        """
        UPLOAD_PATH = config('UPLOAD_PATH')
        delete_files_from_folder(os.path.join(UPLOAD_PATH, 'tenderExcelFiles'))

        if 'financial_data' not in request.files:
            return 'No File in Content', HTTPStatus.NO_CONTENT

        tender_id = request.form['tender_id']
        file = request.files['financial_data']

        if file.filename == '':
            return 'File Not Found', HTTPStatus.NOT_FOUND

        filename = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_PATH, 'tenderExcelFiles/{}'.format(filename)))

        import_tender_data_from_excel(os.path.join(UPLOAD_PATH, 'tenderExcelFiles/{}'.format(filename)), tender_id)

        return 'Excel Data Uploaded Successfully.', HTTPStatus.OK


def import_tender_data_from_excel(file_path, tender_id):
    wb_obj = openpyxl.load_workbook(filename=file_path, data_only=True)

    financialData = wb_obj['DataForm']
    financial_sheet_rows = ['11', '12', '16', '17', '18', '20', '21', '22', '23', '26', '27', '28', '29', '30', '31',
                            '32', '33', '34', '37', '38', '40']
    # deleting old tendering data from db
    TenderFinancialData.query.filter_by(ten_Tender_Id=tender_id).delete()
    db.session.commit()

    for row in financial_sheet_rows:
        tenderFinancialData = TenderFinancialData(
            ten_Tender_Id=tender_id,
            Item=financialData['B{0}'.format(row)].value,
            EquipmentInternal=financialData['C{0}'.format(row)].value,
            EquipmentExternal=financialData['D{0}'.format(row)].value,
            Fuel=financialData['E{0}'.format(row)].value,
            MaterialsPipeline=financialData['F{0}'.format(row)].value,
            MaterialsTeeth=financialData['G{0}'.format(row)].value,
            MaterialsSteel=financialData['H{0}'.format(row)].value,
            MaterialsRock=financialData['I{0}'.format(row)].value,
            MaterialsConcrete=financialData['J{0}'.format(row)].value,
            MaterialsOther=financialData['K{0}'.format(row)].value,
            PersonalLabour=financialData['M{0}'.format(row)].value,
            PersonalStaff=financialData['N{0}'.format(row)].value,
            Misc=financialData['O{0}'.format(row)].value,
            Subcontractor=financialData['P{0}'.format(row)].value,
            MarkupsRisk=financialData['R{0}'.format(row)].value,
            MarkupsOverhead=financialData['S{0}'.format(row)].value,
            MarkupsProfit=financialData['T{0}'.format(row)].value,
            TaxDirect=financialData['V{0}'.format(row)].value,
            TaxIndirect=financialData['W{0}'.format(row)].value,
            Quantities=financialData['Z{0}'.format(row)].value,
            Unit=financialData['AA{0}'.format(row)].value,
            Remarks=financialData['AB{0}'.format(row)].value,
        )

        tenderFinancialData.save()

    equipmentCost = wb_obj['Equipment_CostEstimators']
    equipment_sheet_rows = ['6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '19', '20', '21', '22', '23',
                            '24', '25', '26', '27', '28', '29', '32', '33', '34']
    # deleting old tendering data from db
    TenderEquipmentCost.query.filter_by(ten_Tender_Id=tender_id).delete()
    db.session.commit()

    for row in equipment_sheet_rows:
        tenderEquipmentCost = TenderEquipmentCost(
            ten_Tender_Id=tender_id,
            Item=equipmentCost['A{0}'.format(row)].value,
            NoOfEquipment=equipmentCost['B{0}'.format(row)].value,
            EquipmentDI=equipmentCost['C{0}'.format(row)].value,
            EquipmentDIFixedMR=equipmentCost['D{0}'.format(row)].value,
            EquipmentDIVariableMR=equipmentCost['E{0}'.format(row)].value,
            EquipmentInsurance=equipmentCost['F{0}'.format(row)].value,
            MiscTechOH=equipmentCost['H{0}'.format(row)].value,
            PersonalLabour=equipmentCost['I{0}'.format(row)].value,
            PersonalStaff=equipmentCost['J{0}'.format(row)].value,
            External=equipmentCost['K{0}'.format(row)].value,
        )
        tenderEquipmentCost.save()
    return


def delete_files_from_folder(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
