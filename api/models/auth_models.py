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
            'EmployeeNumber': self.hrEmployee[0].EmployeeNumber.strip(),
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
    dev_AspNetUsersId = db.Column(db.String(450), db.ForeignKey('dbo.AspNetUsers.id', ondelete='CASCADE'))
    tech_EquipmentStatusId = db.Column(db.Integer())

