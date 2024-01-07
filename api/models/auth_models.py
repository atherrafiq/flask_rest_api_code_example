from ..utils.db import db
from datetime import datetime, date, time


class User(db.Model):
    __tablename__ = "AspNetUsers"
    __bind_key__ = 'WebApps'
    __table_args__ = {u'schema': 'dbo'}

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(500), primary_key=False)
    email = db.Column(db.String(500), primary_key=False)
    PasswordHash = db.Column(db.String(500), primary_key=False)
    password = db.Column(db.String(500), primary_key=False)
    active = db.Column(db.Boolean)
    NameFirst = db.Column(db.String(500), primary_key=False)
    NameLast = db.Column(db.String(500), primary_key=False)
    EmployeeNumber = db.Column(db.String(500), primary_key=False)
    FunctionName = db.Column(db.String(500), primary_key=False)
    FullName = db.Column(db.String(500), primary_key=False)

    hrEmployee = db.relationship("Employee")

    @property
    def serialize(self):
        return {
            'Id': self.id,
            'Username': self.username,
            'Email': self.email,
            'Active': self.active,
            'NameFirst': self.NameFirst,
            'NameLast': self.NameLast,
            # 'EmployeeNumber': self.hrEmployee[0].EmployeeNumber.strip() if len(self.hrEmployee) > 0 else '',
            'FunctionName': self.FunctionName,
            'FullName': self.FullName,
        }

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get_or_404(id)


class Employee(db.Model):
    __tablename__ = 'Employee'
    __bind_key__ = 'WebApps'
    __table_args__ = {u'schema': 'hr'}

    Id = db.Column(db.Integer(), primary_key=True)
    EmployeeName = db.Column(db.String(), unique=False)
    EmployeeNumber = db.Column(db.String(450), unique=False)
    EmployeeEmail = db.Column(db.String(50), unique=False)
    gen_CompanyId = db.Column(db.Integer(), unique=False)
    EmployeeTelephone = db.Column(db.String(50), unique=False)
    dev_AspNetUsersId = db.Column(db.String(450), db.ForeignKey('dbo.AspNetUsers.id'))
    tech_EquipmentStatusId = db.Column(db.Integer())

    @property
    def serialize(self):
        return {x: str(self.__dict__[x]) if self.__dict__[x] != None else None for x in self.__dict__ if
                not x.startswith('_')}


class AspNetUserRoles(db.Model):
    __tablename__ = 'AspNetUserRoles'
    __bind_key__ = 'WebApps'
    __table_args__ = {u'schema': 'dbo'}

    UserId = db.Column(db.String())
    RoleId = db.Column(db.String())
    Id = db.Column(db.Integer(), primary_key=True, autoincrement=True)

    @property
    def serialize(self):
        return {x: str(self.__dict__[x]) if self.__dict__[x] != None else None for x in self.__dict__ if
                not x.startswith('_')}


    def save(self):
        db.session.add(self)


class TenderUserRoles(db.Model):
    __tablename__ = 'TenderUserRoles'
    __bind_key__ = 'WebAppsTender'
    __table_args__ = {u'schema': 'ten'}

    Id = db.Column(db.Integer(), primary_key=True)
    RoleName = db.Column(db.String(), unique=False)
    CreatedOn = db.Column(db.DateTime(), default=datetime.now())
    CreatedBy = db.Column(db.String())
    UpdatedOn = db.Column(db.DateTime(), default=datetime.now())
    UpdatedBy = db.Column(db.String())

    @property
    def serialize(self):
        return {x: self.__dict__[x] for x in self.__dict__ if not x.startswith('_')}

    def save(self):
        db.session.add(self)


class TenderUserAssignedRoles(db.Model):
    __tablename__ = 'TenderUserAssignedRoles'
    __bind_key__ = 'WebAppsTender'
    __table_args__ = {u'schema': 'ten'}

    Id = db.Column(db.Integer(), primary_key=True)
    ten_TenderUserRoles_Id = db.Column(db.Integer())
    dev_AspNetUsersId = db.Column(db.String())
    CreatedOn = db.Column(db.DateTime(), default=datetime.now())
    CreatedBy = db.Column(db.String())
    UpdatedOn = db.Column(db.DateTime(), default=datetime.now())
    UpdatedBy = db.Column(db.String())


    @property
    def serialize(self):
        return {x: self.__dict__[x] for x in self.__dict__ if not x.startswith('_')}

    def save(self):
        db.session.add(self)

