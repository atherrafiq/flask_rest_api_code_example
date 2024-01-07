from flask import Flask
from .auth.views import auth_namespace
from .tenders.views import tenders_namespace
from .others.views import others_namespace
from .config.config import config_dict
from .models.auth_models import *
from .models.tenders_models import *
from .utils.db import db
from flask_restx import Api
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_cors import CORS


def create_app(config=config_dict['dev']):

    app = Flask(__name__)
    app.config.from_object(config)

    CORS(app, support_credentials=False)

    authorizations = {
        "Bearer Auth": {
            'type': "apiKey",
            'in': 'header',
            'name': "Authorization",
            'description': "Add a JWT with ** Bearer &lt;JWT&gt; to authorize"
        }
    }

    api = Api(
        app,
        title="Tenders Web API",
        description="A REST API for Tenders Web Application",
        authorizations=authorizations,
        security="Bearer Auth"
    )

    api.add_namespace(tenders_namespace, path='/tenders')
    api.add_namespace(others_namespace, path='/others')
    api.add_namespace(auth_namespace, path='/auth')


    db.init_app(app)
    jwt = JWTManager(app)
    migrate = Migrate(app, db)

    # with app.app_context():
    #     db.create_all()

    @app.shell_context_processor
    def make_shell_context():
        return {
            'db': db,
            # 'User': User,
        }

    return app