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

