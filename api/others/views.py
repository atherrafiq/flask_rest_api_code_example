import http
import json

from flask_restx import Namespace,Resource,fields
from flask_jwt_extended import jwt_required, get_jwt_identity, get_current_user
from ..models.auth_models import *
from ..models.tenders_models import *
from http import HTTPStatus
from ..utils.db import db
from flask import request, jsonify

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from pathlib import Path
from email import encoders

others_namespace = Namespace('others', description="Namespace for others")


@others_namespace.route('/getCountryList')
class getCountryList(Resource):

    @jwt_required()
    def get(self):
        """
            get all countires
        """
        country = Country.query.order_by(Country.Id).all()
        response_data = [x.serialize for x in country]
        return response_data, HTTPStatus.OK


@others_namespace.route('/getNatureOfWorksList')
class getNatureOfWorksList(Resource):

    @jwt_required()
    def get(self):
        """
            get all nature of works
        """
        natureOfWorks = NatureOfWorks.query.order_by(NatureOfWorks.Id).all()
        response_data = [x.serialize for x in natureOfWorks]
        return response_data, HTTPStatus.OK


@others_namespace.route('/getIndustryList')
class getIndustryList(Resource):

    @jwt_required()
    def get(self):
        """
            get all industries
        """
        industry = Industry.query.order_by(Industry.Id).all()
        response_data = [x.serialize for x in industry]
        return response_data, HTTPStatus.OK


@others_namespace.route('/getTenderStatusList')
class getTenderStatusList(Resource):

    @jwt_required()
    def get(self):
        """
            get all tender status
        """
        tenderStatus = TenderStatus.query.order_by(TenderStatus.Id).all()
        response_data = [x.serialize for x in tenderStatus]
        return response_data, HTTPStatus.OK


@others_namespace.route('/getCurrencyList')
class getCurrencyList(Resource):

    @jwt_required()
    def get(self):
        """
            get all currencies
        """
        currency = Currency.query.order_by(Currency.Id).all()
        response_data = [x.serialize for x in currency]
        return response_data, HTTPStatus.OK


@others_namespace.route('/getUserList')
class getUserList(Resource):

    @jwt_required()
    def get(self):
        """
            get all users
        """
        user = User.query.order_by(User.Id).all()
        response_data = [x.serialize for x in user]
        return response_data, HTTPStatus.OK


@others_namespace.route('/getLLCategoryList')
class getLLCategoryList(Resource):

    @jwt_required()
    def get(self):
        """
            get all LL categories
        """
        lLCategory = LLCategory.query.order_by(LLCategory.Id).all()
        response_data = [x.serialize for x in lLCategory]
        return response_data, HTTPStatus.OK


@others_namespace.route('/sendEmail')
class sendEmail(Resource):

    def post(self):
        """
            send email
        """
        data = request.get_json()

        port = 587  # For starttls
        smtp_server = "mail.nmdc.ae"
        sender_email = "webapps@nmdc.ae"
        receiver_email = data['To']
        # password =

        message = MIMEMultipart("alternative")
        message["Subject"] = data['Subject']
        message["From"] = sender_email
        message["To"] = ", ".join(receiver_email)

        body = MIMEText(data['Body'], data['BodyType'])
        message.attach(body)

        with smtplib.SMTP(smtp_server, port) as server:
            server.sendmail(sender_email, receiver_email, message.as_string())

        return 'Email Sent Successfully.', HTTPStatus.OK


@others_namespace.route('/get_user_roles')
class get_user_roles(Resource):

    @jwt_required()
    def get(self):
        """
            get all user roles
        """
        tenderUserRoles = TenderUserRoles.query.all()
        return {'UserRolesList': [x.serialize for x in tenderUserRoles], 'UserRolesDist': {x.Id: x.RoleName for x in tenderUserRoles}}, HTTPStatus.OK


@others_namespace.route('/get_all_users_with_assigned_roles')
class get_all_users_with_assigned_roles(Resource):

    @jwt_required()
    def get(self):
        """
            get all users with assigned roles
        """
        tenderUserAssignedRoles = TenderUserAssignedRoles.query.all()
        response_data = {}

        for userAssignedRole in tenderUserAssignedRoles:
            if userAssignedRole.dev_AspNetUsersId not in response_data:
                response_data[userAssignedRole.dev_AspNetUsersId] = []

            response_data[userAssignedRole.dev_AspNetUsersId].append(userAssignedRole.ten_TenderUserRoles_Id)

        return response_data, HTTPStatus.OK


@others_namespace.route('/assign_user_role')
class assign_user_role(Resource):

    @jwt_required()
    def post(self):
        """
            assign user roles
        """
        data = request.get_json()
        role_ids = [x for x in data['role_ids'].split(',') if x != '']
        TenderUserAssignedRoles.query.filter_by(dev_AspNetUsersId=data['user_id']).delete()

        for role_id in role_ids:
            assignedRoles = TenderUserAssignedRoles(
                ten_TenderUserRoles_Id=role_id,
                dev_AspNetUsersId=data['user_id'],
                UpdatedBy=get_jwt_identity(),
                CreatedBy=get_jwt_identity(),
            )
            assignedRoles.save()

        db.session.commit()

        return 'Role Assigned Successfully.', HTTPStatus.OK


@others_namespace.route('/get_current_user_roles')
class get_current_user_roles(Resource):

    @jwt_required()
    def get(self):
        """
            assign user roles
        """
        user_id = get_jwt_identity()
        tenderUserRoles = TenderUserRoles.query.all()
        tenderUserRoles = {x.Id: x.RoleName for x in tenderUserRoles}
        tenderUserAssignedRoles = TenderUserAssignedRoles.query.filter_by(dev_AspNetUsersId=user_id).all()
        return [tenderUserRoles[x.ten_TenderUserRoles_Id] for x in tenderUserAssignedRoles], HTTPStatus.OK


@others_namespace.route('/getRiskCategory')
class getRiskCategory(Resource):

    @jwt_required()
    def get(self):
        """
            get all risk categories
        """
        riskCategory = RiskCategory.query.order_by(RiskCategory.Id).all()
        response_data = [x.serialize for x in riskCategory]
        return response_data, HTTPStatus.OK


@others_namespace.route('/getLevelOfRisk')
class getLevelOfRisk(Resource):

    @jwt_required()
    def get(self):
        """
            get levels of risk
        """
        levelOfRisk = LevelOfRisk.query.order_by(LevelOfRisk.Id).all()
        response_data = [x.serialize for x in levelOfRisk]
        return response_data, HTTPStatus.OK


@others_namespace.route('/getActivityList')
class getActivityList(Resource):

    @jwt_required()
    def get(self):
        """
            get activity list
        """
        activityList = ActivityList.query.order_by(ActivityList.OrderNumber).all()
        userPositionList = UserPositionList.query.all()
        userPositionList = {x.Id: x.serialize for x in userPositionList}

        response_data = []
        for activity in activityList:
            obj = activity.serialize
            try:
                obj['PositionIdName'] = userPositionList[activity.PositionId]['Name']
            except:
                obj['PositionIdName'] = ''
            response_data.append(obj)
        return response_data, HTTPStatus.OK


@others_namespace.route('/getUserPositionList')
class getUserPositionList(Resource):

    @jwt_required()
    def get(self):
        """
            get user position list
        """
        userPositionList = UserPositionList.query.all()
        response_data = [x.serialize for x in userPositionList]
        return response_data, HTTPStatus.OK


@others_namespace.route('/getUserListwithPositions')
class getUserListwithPositions(Resource):

    @jwt_required()
    def get(self):
        """
            get user list with positions
        """
        userList = UserList.query.all()
        response_data = [x.serialize for x in userList]

        userPositionList = UserPositionList.query.all()
        userPositionList = {x.Id: x.Name for x in userPositionList}

        return {
            'UserList': response_data,
            'UserPositionList': userPositionList,
        }, HTTPStatus.OK


# @others_namespace.route('/getResourceEquipmentMainList')
# class getResourceEquipmentMainList(Resource):
#
#     @jwt_required()
#     def get(self):
#         """
#             get resource equipment main list
#         """
#         resourceEquipmentMain = ResourceEquipmentMain.query.order_by(ResourceEquipmentMain.Id).all()
#         response_data = [x.serialize for x in resourceEquipmentMain]
#         return response_data, HTTPStatus.OK
#
#
# @others_namespace.route('/getResourceManpowerMainList')
# class getResourceManpowerMainList(Resource):
#
#     @jwt_required()
#     def get(self):
#         """
#             get resource manpower main list
#         """
#         resourceManpowerMain = ResourceManpowerMain.query.order_by(ResourceManpowerMain.Id).all()
#         response_data = [x.serialize for x in resourceManpowerMain]
#         return response_data, HTTPStatus.OK


@others_namespace.route('/getMasterUserList')
class getMasterUserList(Resource):

    @jwt_required()
    def get(self):
        """
            get master user list
        """
        user = User.query.all()
        response_data = [x.serialize for x in user]
        return response_data, HTTPStatus.OK