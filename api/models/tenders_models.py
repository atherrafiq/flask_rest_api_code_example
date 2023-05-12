from ..utils.db import db
from datetime import datetime, date, time


class Tenders(db.Model):
    __tablename__ = 'Tenders'
    __bind_key__ = 'WebAppsTender'
    __table_args__ = {u'schema': 'ten'}

    Id = db.Column(db.Integer(), primary_key=True)
    TenderNumber = db.Column(db.String())
    Revision = db.Column(db.Integer())
    TenderRevisionComb = db.Column(db.String())
    MainSub = db.Column(db.String())

    ProjectName = db.Column(db.String())
    Comments = db.Column(db.String())

    Area = db.Column(db.String())
    Location = db.Column(db.String())
    Place = db.Column(db.String())
    ServerFolder = db.Column(db.String())
    Remarks = db.Column(db.String())
    Feedback = db.Column(db.String())

    FuelRate = db.Column(db.Float())

    TenderFromRequired = db.Column(db.Boolean())
    LatestRevision = db.Column(db.Boolean())
    GeoTechnicalDataAvailable = db.Column(db.Boolean())
    SurveyDataAvailable = db.Column(db.Boolean())
    Submission = db.Column(db.String())
    CPC = db.Column(db.Boolean())

    CoordinatesE = db.Column(db.Float())
    CoordinatesN = db.Column(db.Float())
    CoordinatesUTM = db.Column(db.Float())

    CoordinatesLat = db.Column(db.Float())
    CoordinatesLon = db.Column(db.Float())

    Probability = db.Column(db.Integer())
    TenderStatus_Id = db.Column(db.Integer())
    TenderTypeOf = db.Column(db.String())

    SubmissionCurrency_Id = db.Column(db.Integer())

    Country_Id = db.Column(db.Integer())
    Employer_Id = db.Column(db.String())
    Industry_Id = db.Column(db.Integer())
    NatureOfWork_Id = db.Column(db.Integer())

    PrimaryCostEstimator_Id = db.Column(db.String())
    SecondaryCostEstimator_Id = db.Column(db.String())
    DredgingProdEstimator_Id = db.Column(db.String())
    TenderCoordinator_Id = db.Column(db.String())
    Planner_Id = db.Column(db.String())
    Quotations_Id = db.Column(db.Integer())

    TenderDocumentsReceived = db.Column(db.Date())
    DecisionToTender = db.Column(db.Date())
    DecisionToTender = db.Column(db.Date())
    KickOff = db.Column(db.Date())
    Workshop = db.Column(db.Date())
    FinalTenderReview = db.Column(db.Date())
    SubmissionDate = db.Column(db.Date())
    BidExpiryDate = db.Column(db.Date())
    AwardDate = db.Column(db.Date())

    BidValidity = db.Column(db.Integer())
    TenderDuration = db.Column(db.Integer())
    TenderValuePerDay = db.Column(db.Float())

    AnticipatedStartDate = db.Column(db.Date())
    AnticipatedEndDate = db.Column(db.Date())
    PlanningManualStartDate = db.Column(db.Date())
    PlanningManualEndDate = db.Column(db.Date())

    SubsidiaryBranchMainCompany = db.Column(db.String())
    SubContractor = db.Column(db.String())
    CharterNMDC = db.Column(db.String())
    MainSubJVContract = db.Column(db.String())
    NoOfCompanies = db.Column(db.String())
    ContractorType = db.Column(db.String())
    JointVentureCompany = db.Column(db.String())
    ContractForm = db.Column(db.String())
    ContractType = db.Column(db.String())
    Description = db.Column(db.String())
    MethodOfPayment = db.Column(db.String())

    TenderBond = db.Column(db.Boolean())
    TenderBondPercentage = db.Column(db.Integer())
    TenderBondValue = db.Column(db.Float())
    TenderBondCurrency_Id = db.Column(db.Integer())
    TenderBondReturned = db.Column(db.Boolean())
    TenderBondValidity = db.Column(db.Date())

    PerformanceBond = db.Column(db.Boolean())
    PerformanceBondPercentage = db.Column(db.Integer())
    PerformanceBondValue = db.Column(db.Float())
    PerformanceBondCurrency_Id = db.Column(db.Integer())

    RetentionBond = db.Column(db.Boolean())
    RetentionBondPercentage = db.Column(db.Integer())
    RetentionBondValue = db.Column(db.Float())
    RetentionBondCurrency_Id = db.Column(db.Integer())

    WarrantyBond = db.Column(db.Boolean())
    WarrantyBondPercentage = db.Column(db.Integer())
    WarrantyBondValue = db.Column(db.Float())
    WarrantyBondCurrency_Id = db.Column(db.Integer())

    AdvancePaymentGurantee = db.Column(db.Boolean())
    AdvancePaymentGuranteePercentage = db.Column(db.Integer())
    AdvancePaymentGuranteeValue = db.Column(db.Float())
    AdvancePaymentGuranteeCurrency_Id = db.Column(db.Integer())

    ParentPaymentGurantee = db.Column(db.Boolean())
    ParentPaymentGuranteePercentage = db.Column(db.Integer())
    ParentPaymentGuranteeValue = db.Column(db.Float())
    ParentPaymentGuranteeCurrency_Id = db.Column(db.Integer())

    CorporateGurantee = db.Column(db.Boolean())
    CorporateGuranteePercentage = db.Column(db.Integer())
    CorporateGuranteeValue = db.Column(db.Float())
    CorporateGuranteeCurrency_Id = db.Column(db.Integer())

    PaymentGurantee = db.Column(db.Boolean())
    PaymentGuranteePercentage = db.Column(db.Integer())
    PaymentGuranteeValue = db.Column(db.Float())
    PaymentGuranteeCurrency_Id = db.Column(db.Integer())

    tenderLogs = db.relationship("TenderLogs")
    lessonsLearned = db.relationship("LessonsLearned")
    tenderFinancialData = db.relationship("TenderFinancialData")
    tenderEquipmentCost = db.relationship("TenderEquipmentCost")


    @property
    def serialize(self):

        response = {}
        for x in self.__dict__:
            if not x.startswith('_'):
                if self.__dict__[x] != None:
                    if isinstance(self.__dict__[x], date):
                        _date = self.__dict__[x].strftime("%m/%d/%Y")
                        if _date == '01/01/1900':
                            response[x] = ''
                        else:
                            response[x] = _date
                    else:
                        response[x] = self.__dict__[x]
                else:
                    response[x] = ''

        return response

    def save(self):
        db.session.add(self)
        db.session.commit()


class LessonsLearned(db.Model):
    __tablename__ = 'LessonsLearned'
    __bind_key__ = 'WebAppsTender'
    __table_args__ = {u'schema': 'ten'}

    Id = db.Column(db.Integer(), primary_key=True)
    ten_Tender_Id = db.Column(db.Integer(), db.ForeignKey('ten.Tenders.Id'))
    Category = db.Column(db.String())
    Person = db.Column(db.String())
    Subject = db.Column(db.String())
    LessonLearned = db.Column(db.String())
    Remarks = db.Column(db.String())

    @property
    def serialize(self):
        return {x: self.__dict__[x] if self.__dict__[x] != None else None for x in self.__dict__ if not x.startswith('_')}

    def save(self):
        db.session.add(self)

class TenderLogs(db.Model):
    __tablename__ = 'TenderLogs'
    __bind_key__ = 'WebAppsTender'
    __table_args__ = {u'schema': 'ten'}

    Id = db.Column(db.Integer(), primary_key=True)
    ten_Tender_Id = db.Column(db.Integer(), db.ForeignKey('ten.Tenders.Id'))
    FieldName = db.Column(db.String())
    ValueBefore = db.Column(db.String())
    ValueAfter = db.Column(db.String())
    DateTime = db.Column(db.DateTime(), default=datetime.now())
    UpdatedBy_Id = db.Column(db.String())

    @property
    def serialize(self):
        return {x: str(self.__dict__[x]) if self.__dict__[x] != None else None for x in self.__dict__ if not x.startswith('_')}

    def save(self):
        db.session.add(self)
        db.session.commit()


class Country(db.Model):
    __tablename__ = 'Country'
    __bind_key__ = 'WebAppsTender'
    __table_args__ = {u'schema': 'dbo'}

    Id = db.Column(db.Integer(), primary_key=True)
    CountryName = db.Column(db.String())
    CountryISO = db.Column(db.String())

    @property
    def serialize(self):
        return {x: str(self.__dict__[x]) if self.__dict__[x] != None else None for x in self.__dict__ if not x.startswith('_')}

    def save(self):
        db.session.add(self)
        db.session.commit()


class NatureOfWorks(db.Model):
    __tablename__ = 'NatureOfWorks'
    __bind_key__ = 'WebAppsTender'
    __table_args__ = {u'schema': 'dbo'}

    Id = db.Column(db.Integer(), primary_key=True)
    NatureOfWorkName = db.Column(db.String())

    @property
    def serialize(self):
        return {x: str(self.__dict__[x]) if self.__dict__[x] != None else None for x in self.__dict__ if not x.startswith('_')}

    def save(self):
        db.session.add(self)
        db.session.commit()


class Industry(db.Model):
    __tablename__ = 'Industry'
    __bind_key__ = 'WebAppsTender'
    __table_args__ = {u'schema': 'dbo'}

    Id = db.Column(db.Integer(), primary_key=True)
    IndustryName = db.Column(db.String())

    @property
    def serialize(self):
        return {x: str(self.__dict__[x]) if self.__dict__[x] != None else None for x in self.__dict__ if not x.startswith('_')}

    def save(self):
        db.session.add(self)
        db.session.commit()


class TenderStatus(db.Model):
    __tablename__ = 'TenderStatus'
    __bind_key__ = 'WebAppsTender'
    __table_args__ = {u'schema': 'dbo'}

    Id = db.Column(db.Integer(), primary_key=True)
    TenderStatusName = db.Column(db.String())

    @property
    def serialize(self):
        return {x: str(self.__dict__[x]) if self.__dict__[x] != None else None for x in self.__dict__ if not x.startswith('_')}

    def save(self):
        db.session.add(self)
        db.session.commit()


class Currency(db.Model):
    __tablename__ = 'Currency'
    __bind_key__ = 'WebAppsTender'
    __table_args__ = {u'schema': 'dbo'}

    Id = db.Column(db.Integer(), primary_key=True)
    CurrencyName = db.Column(db.String())

    @property
    def serialize(self):
        return {x: str(self.__dict__[x]) if self.__dict__[x] != None else None for x in self.__dict__ if not x.startswith('_')}

    def save(self):
        db.session.add(self)
        db.session.commit()


class TenderFinancialData(db.Model):
    __tablename__ = 'TenderFinancialData'
    __bind_key__ = 'WebAppsTender'
    __table_args__ = {u'schema': 'ten'}

    Id = db.Column(db.Integer(), primary_key=True)
    ten_TenderId = db.Column(db.Integer(), db.ForeignKey('ten.Tenders.Id'))
    ten_EquipmentCostItemId = db.Column(db.Integer())

    EquipmentEME = db.Column(db.Float())
    EquipmentInternal = db.Column(db.Float())
    EquipmentExternal = db.Column(db.Float())
    Fuel = db.Column(db.Float())
    MaterialsPipeline = db.Column(db.Float())
    MaterialsTeeth = db.Column(db.Float())
    MaterialsSteel = db.Column(db.Float())
    MaterialsRock = db.Column(db.Float())
    MaterialsImportedFill = db.Column(db.Float())
    MaterialsGeotextile = db.Column(db.Float())
    MaterialsConcrete = db.Column(db.Float())
    MaterialsNavAid = db.Column(db.Float())
    MaterialsMarineFurniture = db.Column(db.Float())
    MaterialsOther = db.Column(db.Float())
    PersonalLabour = db.Column(db.Float())
    PersonalStaff = db.Column(db.Float())
    Misc = db.Column(db.Float())
    Subcontractor = db.Column(db.Float())

    MarkupsRisk = db.Column(db.Float())
    MarkupsOverhead = db.Column(db.Float())
    MarkupsProfit = db.Column(db.Float())
    TaxDirect = db.Column(db.Float())
    TaxIndirect = db.Column(db.Float())

    Quantity = db.Column(db.Float())
    Unit = db.Column(db.String())
    Remarks = db.Column(db.String())
    IsArchived = db.Column(db.Boolean())
    CreatedBy = db.Column(db.String())
    CreatedOn = db.Column(db.DateTime())

    @property
    def serialize(self):
        response = {'AED': '', 'Item': '', 'IsParent': ''}
        for x in self.__dict__:
            if not x.startswith('_'):
                if isinstance(self.__dict__[x], float) and self.__dict__[x] is not None:
                    response[x] = round(self.__dict__[x])
                elif isinstance(self.__dict__[x], datetime) and self.__dict__[x] is not None:
                    response[x] = self.__dict__[x].strftime("%m/%d/%Y, %H:%M:%S")
                elif self.__dict__[x] is None:
                    response[x] = 0
                else:
                    response[x] = self.__dict__[x]

        response['TotalCost'] = response['EquipmentInternal'] + response['EquipmentExternal'] + response['EquipmentEME']+ \
                                response['Fuel'] + response['MaterialsPipeline'] + response['MaterialsTeeth'] + \
                                response['MaterialsSteel'] + response['MaterialsRock'] + response['MaterialsImportedFill'] + \
                                response['MaterialsGeotextile'] + response['MaterialsConcrete'] + response['MaterialsNavAid'] + \
                                response['MaterialsMarineFurniture'] + response['MaterialsOther'] + response['PersonalLabour'] + \
                                response['PersonalStaff'] + response['Misc'] + response['Subcontractor']

        response['TotalTaxExcl'] = response['MarkupsRisk'] + response['MarkupsOverhead'] + response['MarkupsProfit']
        response['TotalTaxIncl'] = response['TaxDirect'] + response['TaxIndirect']

        return response

    def save(self):
        db.session.add(self)
        db.session.commit()


class EquipmentCostItem(db.Model):
    __tablename__ = 'EquipmentCostItem'
    __bind_key__ = 'WebAppsTender'
    __table_args__ = {u'schema': 'ten'}

    Id = db.Column(db.Integer(), primary_key=True)
    ParentId = db.Column(db.Integer())
    Item = db.Column(db.String())
    ItemReference = db.Column(db.String())

    @property
    def serialize(self):
        return {x: self.__dict__[x] for x in self.__dict__ if not x.startswith('_')}


class TenderEquipmentCost(db.Model):
    __tablename__ = 'TenderEquipmentCost'
    __bind_key__ = 'WebAppsTender'
    __table_args__ = {u'schema': 'ten'}

    Id = db.Column(db.Integer(), primary_key=True)
    ten_Tender_Id = db.Column(db.Integer(), db.ForeignKey('ten.Tenders.Id'))

    Item = db.Column(db.String())
    NoOfEquipment = db.Column(db.Integer())
    EquipmentDI = db.Column(db.Float())
    EquipmentDIFixedMR = db.Column(db.Float())
    EquipmentDIVariableMR = db.Column(db.Float())
    EquipmentInsurance = db.Column(db.Float())
    MiscTechOH = db.Column(db.Float())
    PersonalStaff = db.Column(db.Float())
    PersonalLabour = db.Column(db.Float())
    External = db.Column(db.Float())

    @property
    def serialize(self):
        response = {}
        for x in self.__dict__:
            if not x.startswith('_'):
                if isinstance(self.__dict__[x], float) and self.__dict__[x] is not None:
                    response[x] = round(self.__dict__[x])
                elif self.__dict__[x] is None:
                    response[x] = 0
                else:
                    response[x] = self.__dict__[x]

        response['TotalInternal'] = response['EquipmentDI'] + response['EquipmentDIFixedMR'] + \
                                    response['EquipmentDIVariableMR'] + response['EquipmentInsurance']
        response['TotalEquipment'] = response['TotalInternal'] + response['External']
        return response

    def save(self):
        db.session.add(self)
        db.session.commit()
