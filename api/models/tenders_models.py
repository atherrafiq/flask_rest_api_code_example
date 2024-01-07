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
    ExchangeCurrency_Id = db.Column(db.Integer())

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

    TenderSplitType = db.Column(db.Integer())

    IsArchive = db.Column(db.Boolean())
    KMZFile = db.Column(db.String())
    ScopeBriefFile = db.Column(db.String())
    TenderEvaluationFromFile = db.Column(db.String())
    ScopeNarrative = db.Column(db.String())
    FinancialInEightFileLink = db.Column(db.String())
    In8FileName = db.Column(db.String())

    CivilMarineEPC = db.Column(db.Float())
    GIPillingWorks = db.Column(db.Float())
    Dredging = db.Column(db.Float())

    tenderLogs = db.relationship("TenderLogs")
    lessonsLearned = db.relationship("LessonsLearned")
    planning = db.relationship("Planning")
    tenderFinancialData = db.relationship("TenderFinancialData")
    tenderEquipmentCost = db.relationship("TenderEquipmentCost")
    riskRegister = db.relationship("RiskRegister")
    tenderActivityRegister = db.relationship("TenderActivityRegister")
    tenderSubmissionDates = db.relationship("TenderSubmissionDates")


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


class TenderSubmissionDates(db.Model):
    __tablename__ = 'TenderSubmissionDates'
    __bind_key__ = 'WebAppsTender'
    __table_args__ = {u'schema': 'ten'}

    Id = db.Column(db.Integer(), primary_key=True)
    Remarks = db.Column(db.String())
    SubmissionDate = db.Column(db.Date())
    ten_Tender_Id = db.Column(db.Integer(), db.ForeignKey('ten.Tenders.Id'))

    @property
    def serialize(self):
        return {x: str(self.__dict__[x]) if self.__dict__[x] != None else None for x in self.__dict__ if not x.startswith('_')}

    def save(self):
        db.session.add(self)
        db.session.commit()


class LessonsLearned(db.Model):
    __tablename__ = 'LessonsLearned'
    __bind_key__ = 'WebAppsTender'
    __table_args__ = {u'schema': 'ten'}

    Id = db.Column(db.Integer(), primary_key=True)
    ten_Tender_Id = db.Column(db.Integer(), db.ForeignKey('ten.Tenders.Id'))
    ten_LLCategoryId = db.Column(db.INTEGER())
    Person = db.Column(db.VARCHAR(max))
    Subject = db.Column(db.VARCHAR(max))
    LessonLearned = db.Column(db.VARCHAR(max))
    Remarks = db.Column(db.VARCHAR(max))

    @property
    def serialize(self):
        return {x: self.__dict__[x] if self.__dict__[x] != None else None for x in self.__dict__ if not x.startswith('_')}

    def save(self):
        db.session.add(self)


class Planning(db.Model):
    __tablename__ = 'Planning'
    __bind_key__ = 'WebAppsTender'
    __table_args__ = {u'schema': 'ten'}

    Id = db.Column(db.Integer(), primary_key=True)
    ten_Tender_Id = db.Column(db.Integer(), db.ForeignKey('ten.Tenders.Id'))
    ten_EquipmentCostItemId = db.Column(db.Integer())
    DateStart = db.Column(db.Date())
    DateFinish = db.Column(db.Date())
    CreatedBy = db.Column(db.String())
    CreatedOn = db.Column(db.DateTime())

    @property
    def serialize(self):
        response = {}
        for x in self.__dict__:
            if not x.startswith('_'):
                if self.__dict__[x] != None:
                    if isinstance(self.__dict__[x], date):
                        _date = self.__dict__[x].strftime("%m/%d/%Y")
                        if _date == '01/01/1900':
                            response[x] = None
                        else:
                            response[x] = _date
                    else:
                        response[x] = self.__dict__[x]
                else:
                    response[x] = self.__dict__[x]
        return response

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
    ClassName = db.Column(db.String())

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
    EstimatedCost = db.Column(db.Float())

    Contingencies = db.Column(db.Float())
    TotalCost = db.Column(db.Float())

    MarkupsRiskPercent = db.Column(db.Float())
    MarkupsOverheadPercent = db.Column(db.Float())
    MarkupsProfitPercent = db.Column(db.Float())

    MarkupsRisk = db.Column(db.Float())
    MarkupsOverhead = db.Column(db.Float())
    MarkupsProfit = db.Column(db.Float())
    TaxDirect = db.Column(db.Float())
    TaxIndirect = db.Column(db.Float())

    TotalCost_exclTax = db.Column(db.Float())
    TotalCost_inclTax = db.Column(db.Float())

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
    Child = db.Column(db.Integer())
    SubChild = db.Column(db.Integer())

    @property
    def serialize(self):
        return {x: self.__dict__[x] for x in self.__dict__ if not x.startswith('_')}


class EquipmentItem(db.Model):
    __tablename__ = 'EquipmentItem'
    __bind_key__ = 'WebAppsTender'
    __table_args__ = {u'schema': 'ten'}

    Id = db.Column(db.Integer(), primary_key=True)
    Item = db.Column(db.String())
    ParentId = db.Column(db.Integer())
    IsMarineEquipment = db.Column(db.Integer())

    @property
    def serialize(self):
        return {x: self.__dict__[x] for x in self.__dict__ if not x.startswith('_')}


class TenderEquipmentCost(db.Model):
    __tablename__ = 'TenderEquipmentCost'
    __bind_key__ = 'WebAppsTender'
    __table_args__ = {u'schema': 'ten'}

    Id = db.Column(db.Integer(), primary_key=True)
    ten_Tender_Id = db.Column(db.Integer(), db.ForeignKey('ten.Tenders.Id'))
    ten_EquipmentItemId = db.Column(db.Integer())

    NoOfEquipment = db.Column(db.Integer())
    EquipmentDI = db.Column(db.Float())
    EquipmentDIFixedMR = db.Column(db.Float())
    EquipmentDIVariableMR = db.Column(db.Float())
    EquipmentInsurance = db.Column(db.Float())

    MiscTechOH = db.Column(db.Float())
    PersonalStaff = db.Column(db.Float())
    PersonalLabour = db.Column(db.Float())
    External = db.Column(db.Float())

    Fuel = db.Column(db.Float())
    Pipeline = db.Column(db.Float())
    Teeth = db.Column(db.Float())
    Others = db.Column(db.Float())
    Food = db.Column(db.Float())
    Accomodation = db.Column(db.Float())
    Transport = db.Column(db.Float())
    TotalCost = db.Column(db.Float())
    IsDredging = db.Column(db.Boolean())
    CreatedBy = db.Column(db.String())
    CreatedOn = db.Column(db.DateTime())

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

        response['TotalEquipment'] = response['TotalInternal'] + response['External'] + response['MiscTechOH'] + response['PersonalStaff'] + response['PersonalLabour']
        return response

    def save(self):
        db.session.add(self)
        db.session.commit()


class EquipmentItemDrdgMap(db.Model):            
    __tablename__ = 'EquipmentItemDrdgMap'            
    __bind_key__ = 'WebAppsTender'            
    __table_args__ = {u'schema': 'ten'}
    Id = db.Column(db.INTEGER(), primary_key=True)
    ten_EquipmentItemId = db.Column(db.INTEGER())
    DrdgEquipmentName = db.Column(db.VARCHAR(max))
    CreatedBy = db.Column(db.VARCHAR(max))
    CreatedOn = db.Column(db.DATETIME())


class RiskCategory(db.Model):
    __tablename__ = 'RiskCategory'
    __bind_key__ = 'WebAppsTender'
    __table_args__ = {u'schema': 'ten'}

    Id = db.Column(db.Integer(), primary_key=True)
    Category = db.Column(db.String())

    @property
    def serialize(self):
        return {x: self.__dict__[x] for x in self.__dict__ if not x.startswith('_')}

    def save(self):
        db.session.add(self)
        db.session.commit()


class LevelOfRisk(db.Model):
    __tablename__ = 'LevelOfRisk'
    __bind_key__ = 'WebAppsTender'
    __table_args__ = {u'schema': 'ten'}

    Id = db.Column(db.Integer(), primary_key=True)
    Likelihood = db.Column(db.Integer())
    Consequence = db.Column(db.Integer())
    RiskNumber = db.Column(db.String())
    Color = db.Column(db.String())

    @property
    def serialize(self):
        return {x: self.__dict__[x] for x in self.__dict__ if not x.startswith('_')}

    def save(self):
        db.session.add(self)
        db.session.commit()


class RiskRegister(db.Model):
    __tablename__ = 'RiskRegister'
    __bind_key__ = 'WebAppsTender'
    __table_args__ = {u'schema': 'ten'}

    Id = db.Column(db.Integer(), primary_key=True)
    ten_TenderId = db.Column(db.Integer(), db.ForeignKey('ten.Tenders.Id'))
    IsRisk = db.Column(db.Boolean())
    IsFixed = db.Column(db.Boolean())
    ten_RiskCategory = db.Column(db.Integer())
    RiskElement = db.Column(db.String())
    EventDetails = db.Column(db.String())
    ConsequenceDetails = db.Column(db.String())
    ten_LevelOfRiskId_initial = db.Column(db.Integer())
    TreatmentMitigation = db.Column(db.String())
    ten_LevelOfRiskId_residual = db.Column(db.Integer())
    ImplementationStatus = db.Column(db.String())
    RiskValue = db.Column(db.Float())
    Probability = db.Column(db.Float())
    RiskAllowance = db.Column(db.Float())
    CreatedBy = db.Column(db.String())
    CreatedOn = db.Column(db.DATETIME())
    UpdatedBy = db.Column(db.String())
    UpdatedOn = db.Column(db.DATETIME())

    @property
    def serialize(self):
        return {x: str(self.__dict__[x]) if self.__dict__[x] != None else None for x in self.__dict__ if
                not x.startswith('_')}

    def save(self):
        db.session.add(self)
        db.session.commit()


class ActivityList(db.Model):
    __tablename__ = 'ActivityList'
    __bind_key__ = 'WebAppsTender'
    __table_args__ = {u'schema': 'ten'}

    Id = db.Column(db.Integer(), primary_key=True)
    Name = db.Column(db.String())
    OrderNumber = db.Column(db.Integer())
    PositionId = db.Column(db.Integer())
    CreatedBy = db.Column(db.String())
    CreatedOn = db.Column(db.DATETIME())

    @property
    def serialize(self):
        return {x: str(self.__dict__[x]) if self.__dict__[x] != None else None for x in self.__dict__ if
                not x.startswith('_')}

    def save(self):
        db.session.add(self)
        db.session.commit()


class TenderActivityRegister(db.Model):
    __tablename__ = 'TenderActivityRegister'
    __bind_key__ = 'WebAppsTender'
    __table_args__ = {u'schema': 'ten'}

    Id = db.Column(db.Integer(), primary_key=True)
    ten_TenderId = db.Column(db.Integer(), db.ForeignKey('ten.Tenders.Id'))
    ten_ActivityListId = db.Column(db.Integer())
    ten_UserListId = db.Column(db.Integer())
    Deadline = db.Column(db.DATETIME())
    Status = db.Column(db.Boolean())
    CreatedBy = db.Column(db.String())
    CreatedOn = db.Column(db.DATETIME())
    UpdatedBy = db.Column(db.String())
    UpdatedOn = db.Column(db.DATETIME())
    emailTriggered = db.Column(db.Boolean())

    @property
    def serialize(self):
        return {x: str(self.__dict__[x]) if self.__dict__[x] != None else None for x in self.__dict__ if
                not x.startswith('_')}

    def save(self):
        db.session.add(self)
        db.session.commit()


class UserList(db.Model):
    __tablename__ = 'UserList'
    __bind_key__ = 'WebAppsTender'
    __table_args__ = {u'schema': 'ten'}

    Id = db.Column(db.Integer(), primary_key=True)
    Name = db.Column(db.String())
    ten_UserPositionListId = db.Column(db.Integer())
    dbo_AspNetUsersId = db.Column(db.String())
    CreatedBy = db.Column(db.String())
    CreatedOn = db.Column(db.DATETIME())
    UpdatedBy = db.Column(db.String())
    UpdatedOn = db.Column(db.DATETIME())

    @property
    def serialize(self):
        return {x: str(self.__dict__[x]) if self.__dict__[x] != None else None for x in self.__dict__ if
                not x.startswith('_')}

    def save(self):
        db.session.add(self)
        db.session.commit()


class UserPositionList(db.Model):
    __tablename__ = 'UserPositionList'
    __bind_key__ = 'WebAppsTender'
    __table_args__ = {u'schema': 'ten'}

    Id = db.Column(db.Integer(), primary_key=True)
    Name = db.Column(db.String())
    CreatedBy = db.Column(db.String())
    CreatedOn = db.Column(db.DATETIME())
    UpdatedBy = db.Column(db.String())
    UpdatedOn = db.Column(db.DATETIME())

    @property
    def serialize(self):
        return {x: str(self.__dict__[x]) if self.__dict__[x] != None else None for x in self.__dict__ if
                not x.startswith('_')}

    def save(self):
        db.session.add(self)
        db.session.commit()


class LLCategory(db.Model):
    __tablename__ = 'LLCategory'
    __bind_key__ = 'WebAppsTender'
    __table_args__ = {u'schema': 'ten'}

    Id = db.Column(db.Integer(), primary_key=True)
    Category = db.Column(db.String())

    @property
    def serialize(self):
        return {x: str(self.__dict__[x]) if self.__dict__[x] != None else None for x in self.__dict__ if not x.startswith('_')}

    def save(self):
        db.session.add(self)
        db.session.commit()


class ResourceCode(db.Model):
    __tablename__ = 'ResourceCode'
    __bind_key__ = 'WebAppsTender'
    __table_args__ = {u'schema': 'ten'}
    Id = db.Column(db.INTEGER(), primary_key=True)
    Name = db.Column(db.VARCHAR(max))
    Tag = db.Column(db.VARCHAR(max))
    CreatedBy = db.Column(db.VARCHAR(max))
    CreatedOn = db.Column(db.DATETIME())

    @property
    def serialize(self):
        return {x: str(self.__dict__[x]) if self.__dict__[x] != None else None for x in self.__dict__ if
                not x.startswith('_')}

    def save(self):
        db.session.add(self)
        db.session.commit()


class ResourceDepartment(db.Model):
    __tablename__ = 'ResourceDepartment'
    __bind_key__ = 'WebAppsTender'
    __table_args__ = {u'schema': 'ten'}

    Id = db.Column(db.Integer(), primary_key=True)
    Name = db.Column(db.String())
    Psix_Reference = db.Column(db.String())
    CreatedBy = db.Column(db.String())
    CreatedOn = db.Column(db.DATETIME())

    @property
    def serialize(self):
        return {x: str(self.__dict__[x]) if self.__dict__[x] != None else None for x in self.__dict__ if
                not x.startswith('_')}

    def save(self):
        db.session.add(self)
        db.session.commit()


class ResourceEquipment(db.Model):
    __tablename__ = 'ResourceEquipment'
    __bind_key__ = 'WebAppsTender'
    __table_args__ = {u'schema': 'ten'}

    Id = db.Column(db.Integer(), primary_key=True)
    Name = db.Column(db.String())
    ten_ResourceEquipmentLevelId_1 = db.Column(db.Integer())
    ten_ResourceEquipmentLevelId_2 = db.Column(db.Integer())
    ten_ResourceEquipmentLevelId_3 = db.Column(db.Integer())
    ten_ResourceDepartmentId = db.Column(db.Integer())
    ten_ResourceCodeId = db.Column(db.Integer())
    CreatedBy = db.Column(db.String())
    CreatedOn = db.Column(db.DATETIME())

    @property
    def serialize(self):
        return {x: str(self.__dict__[x]) if self.__dict__[x] != None else None for x in self.__dict__ if
                not x.startswith('_')}

    def save(self):
        db.session.add(self)
        db.session.commit()


class ResourceEquipmentLevel(db.Model):
    __tablename__ = 'ResourceEquipmentLevel'
    __bind_key__ = 'WebAppsTender'
    __table_args__ = {u'schema': 'ten'}

    Id = db.Column(db.Integer(), primary_key=True)
    Name = db.Column(db.String())
    LevelNumber = db.Column(db.Integer())
    CreatedBy = db.Column(db.String())
    CreatedOn = db.Column(db.DATETIME())

    @property
    def serialize(self):
        return {x: str(self.__dict__[x]) if self.__dict__[x] != None else None for x in self.__dict__ if
                not x.startswith('_')}

    def save(self):
        db.session.add(self)
        db.session.commit()


class ResourceManpower(db.Model):
    __tablename__ = 'ResourceManpower'
    __bind_key__ = 'WebAppsTender'
    __table_args__ = {u'schema': 'ten'}

    Id = db.Column(db.Integer(), primary_key=True)
    Name = db.Column(db.String())
    ten_ResourceManpowerLevelId_1 = db.Column(db.Integer())
    ten_ResourceManpowerLevelId_2 = db.Column(db.Integer())
    ten_ResourceManpowerLevelId_3 = db.Column(db.Integer())
    ten_ResourceManpowerLevelId_4 = db.Column(db.Integer())
    ten_ResourceManpowerLevelId_5 = db.Column(db.Integer())
    ten_ResourceDepartmentId = db.Column(db.Integer())
    ten_ResourceCodeId = db.Column(db.Integer())
    CreatedBy = db.Column(db.String())
    CreatedOn = db.Column(db.DATETIME())

    @property
    def serialize(self):
        return {x: str(self.__dict__[x]) if self.__dict__[x] != None else None for x in self.__dict__ if
                not x.startswith('_')}

    def save(self):
        db.session.add(self)
        db.session.commit()


class ResourceManpowerLevel(db.Model):
    __tablename__ = 'ResourceManpowerLevel'
    __bind_key__ = 'WebAppsTender'
    __table_args__ = {u'schema': 'ten'}

    Id = db.Column(db.Integer(), primary_key=True)
    Name = db.Column(db.String())
    LevelNumber = db.Column(db.Integer())
    CreatedBy = db.Column(db.String())
    CreatedOn = db.Column(db.DATETIME())

    @property
    def serialize(self):
        return {x: str(self.__dict__[x]) if self.__dict__[x] != None else None for x in self.__dict__ if
                not x.startswith('_')}

    def save(self):
        db.session.add(self)
        db.session.commit()


class ResourceMaterial(db.Model):
    __tablename__ = 'ResourceMaterial'
    __bind_key__ = 'WebAppsTender'
    __table_args__ = {u'schema': 'ten'}

    Id = db.Column(db.Integer(), primary_key=True)
    Name = db.Column(db.String())
    ten_ResourceMaterialLevelId_1 = db.Column(db.Integer())
    dbo_UnitId = db.Column(db.Integer())
    CreatedBy = db.Column(db.String())
    CreatedOn = db.Column(db.DATETIME())

    @property
    def serialize(self):
        return {x: str(self.__dict__[x]) if self.__dict__[x] != None else None for x in self.__dict__ if
                not x.startswith('_')}

    def save(self):
        db.session.add(self)
        db.session.commit()


class ResourceMaterialLevel(db.Model):
    __tablename__ = 'ResourceMaterialLevel'
    __bind_key__ = 'WebAppsTender'
    __table_args__ = {u'schema': 'ten'}

    Id = db.Column(db.Integer(), primary_key=True)
    Name = db.Column(db.String())
    LevelNumber = db.Column(db.Integer())
    CreatedBy = db.Column(db.String())
    CreatedOn = db.Column(db.DATETIME())

    @property
    def serialize(self):
        return {x: str(self.__dict__[x]) if self.__dict__[x] != None else None for x in self.__dict__ if
                not x.startswith('_')}

    def save(self):
        db.session.add(self)
        db.session.commit()


class Unit(db.Model):
    __tablename__ = 'Unit'
    __bind_key__ = 'WebAppsTender'
    __table_args__ = {u'schema': 'dbo'}

    Id = db.Column(db.Integer(), primary_key=True)
    Name = db.Column(db.String())
    CreatedBy = db.Column(db.String())
    CreatedOn = db.Column(db.DATETIME())

    @property
    def serialize(self):
        return {x: str(self.__dict__[x]) if self.__dict__[x] != None else None for x in self.__dict__ if
                not x.startswith('_')}

    def save(self):
        db.session.add(self)
        db.session.commit()


class ManpowerHistogram(db.Model):
    __tablename__ = 'ManpowerHistogram'
    __bind_key__ = 'WebAppsTender'
    __table_args__ = {u'schema': 'ten'}

    Id = db.Column(db.INTEGER(), primary_key=True)
    ten_TendersId = db.Column(db.INTEGER())
    ten_ResourceManpowerId = db.Column(db.INTEGER())
    DateStart = db.Column(db.DATE())
    DateFinish = db.Column(db.DATE())
    Value = db.Column(db.FLOAT())
    CreatedBy = db.Column(db.VARCHAR(max))
    CreatedOn = db.Column(db.DATETIME())

    @property
    def serialize(self):
        return {x: str(self.__dict__[x]) if self.__dict__[x] != None else None for x in self.__dict__ if
                not x.startswith('_')}

    def save(self):
        db.session.add(self)
        db.session.commit()


class EquipmentHistogram(db.Model):
    __tablename__ = 'EquipmentHistogram'
    __bind_key__ = 'WebAppsTender'
    __table_args__ = {u'schema': 'ten'}

    Id = db.Column(db.INTEGER(), primary_key=True)
    ten_TendersId = db.Column(db.INTEGER())
    ten_ResourceEquipmentId = db.Column(db.INTEGER())
    DateStart = db.Column(db.DATE())
    DateFinish = db.Column(db.DATE())
    Value = db.Column(db.FLOAT())
    CreatedBy = db.Column(db.VARCHAR(max))
    CreatedOn = db.Column(db.DATETIME())

    @property
    def serialize(self):
        return {x: str(self.__dict__[x]) if self.__dict__[x] != None else None for x in self.__dict__ if
                not x.startswith('_')}

    def save(self):
        db.session.add(self)
        db.session.commit()


class MaterialHistogram(db.Model):
    __tablename__ = 'MaterialHistogram'
    __bind_key__ = 'WebAppsTender'
    __table_args__ = {u'schema': 'ten'}
    Id = db.Column(db.INTEGER(), primary_key=True)
    ten_TendersId = db.Column(db.INTEGER())
    ten_ResourceMaterialId = db.Column(db.INTEGER())
    DateStart = db.Column(db.DATE())
    DateFinish = db.Column(db.DATE())
    Value = db.Column(db.FLOAT())
    CreatedBy = db.Column(db.VARCHAR(max))
    CreatedOn = db.Column(db.DATETIME())

    @property
    def serialize(self):
        return {x: str(self.__dict__[x]) if self.__dict__[x] != None else None for x in self.__dict__ if
                not x.startswith('_')}

    def save(self):
        db.session.add(self)
        db.session.commit()


class OrganizationalCategory(db.Model):
    __tablename__ = 'OrganizationalCategory'
    __bind_key__ = 'WebAppsTender'
    __table_args__ = {u'schema': 'ten'}
    Id = db.Column(db.INTEGER(), primary_key=True)
    OrganizationalCategoryItem = db.Column(db.VARCHAR(max))
    ExcelColumnName = db.Column(db.VARCHAR(max))
    TopSheetItemCode = db.Column(db.VARCHAR(max))
    TopSheetDescRef = db.Column(db.VARCHAR(max))

    @property
    def serialize(self):
        return {x: str(self.__dict__[x]) if self.__dict__[x] != None else None for x in self.__dict__ if
                not x.startswith('_')}

    def save(self):
        db.session.add(self)
        db.session.commit()