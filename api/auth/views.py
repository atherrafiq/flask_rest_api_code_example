import requests
from flask_restx import Resource,Namespace,fields
from flask import request, jsonify
from ..models.auth_models import *
from werkzeug.security import generate_password_hash,check_password_hash
from http import HTTPStatus
from flask_jwt_extended import (create_access_token,
create_refresh_token,jwt_required,get_jwt_identity)
from werkzeug.exceptions import Conflict, BadRequest
from sqlalchemy import and_, or_

auth_namespace = Namespace('auth', description="Namespace for authentication")


# @auth_namespace.route('/signup')
# class SignUp(Resource):
#
#     def post(self):
#         """
#             create a new user account
#         """
#         data = request.get_json()
#
#         user = User.query.filter(
#             or_(
#                 User.Email == data.get('Email'),
#                 User.EmployeeNumber == data.get('EmployeeNumber'),
#             )
#         ).scalar()
#
#         if user:
#             raise Conflict(f"User with Email '{data.get('Email')}' or with Employee Number '{data.get('EmployeeNumber')}' already exists.")
#
#         new_user = User(
#             Email=data.get('Email'),
#             EmployeeNumber=data.get('EmployeeNumber'),
#             FirstName=data.get('FirstName'),
#             LastName=data.get('LastName'),
#             IsActive=1,
#             ContactNumber=data.get('ContactNumber'),
#             PasswordHash=generate_password_hash(data.get('Password'))
#         )
#         new_user.save()
#         return 'User Created Successfully.', HTTPStatus.CREATED


@auth_namespace.route('/generate_python_api_token')
class generate_python_api_token(Resource):

    def post(self):
        """
            generate a JWT token
        """
        data = request.get_json()
        ASP_NET_Token = data.get('ASP_NET_Token')
        App_Id = data.get('App_Id')

        url = 'https://webapps.nmdc.ae/DataAPI/api/Apps/GetUserAppAcces?AppId=' + str(App_Id)
        payload = {}
        headers = {'Authorization': 'Bearer ' + ASP_NET_Token}
        response = requests.request("GET", url, headers=headers, data=payload)

        if response.text is not '':  # access
            access_token = create_access_token(identity=response.text)
            refresh_token = create_refresh_token(identity=response.text)

            user = User.query.filter_by(id=response.text).first()

            response = {
                'access_token': access_token,
                'refresh_token': refresh_token,
                'user': user.serialize,
            }

            return response, HTTPStatus.OK
        raise BadRequest("Invalid AppId or ASP.Net Token.")


# @auth_namespace.route('/login')
# class Login(Resource):
#
#     def post(self):
#         """
#             generate a JWT token
#         """
#         data = request.get_json()
#         Email = data.get('Email')
#         Password = data.get('Password')
#
#         user = User.query.filter_by(email=Email).first()
#
#         if (user is not None) and dotnet_identity_check_password(Email, Password) and user.active is True:
#             access_token = create_access_token(identity=user.id)
#             refresh_token = create_refresh_token(identity=user.id)
#
#             response = {
#                 'acccess_token': access_token,
#                 'refresh_token': refresh_token
#             }
#
#             return response, HTTPStatus.OK
#         raise BadRequest("Invalid Username or password")
#
#
# def dotnet_identity_check_password(userName, password):
#     url = 'https://webapps.nmdc.ae/DataAPI/api/ApplicationUser/Login'
#     payload = {"userName": userName, "password": password}
#     response = requests.post(url, json=payload)
#     if response.status_code is 200:
#         return True
#     else:
#         return False


@auth_namespace.route('/refresh')
class Refresh(Resource):

    @jwt_required(refresh=True)
    def post(self):
        """
            refresh user token
        """
        Id = get_jwt_identity()
        access_token = create_access_token(identity=Id)
        return {'access_token': access_token}, HTTPStatus.OK
        


