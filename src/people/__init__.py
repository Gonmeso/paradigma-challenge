from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restplus import Api
import people.config


app = Flask(__name__)
app.config.from_object(config.Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from people.v1.api import api as people_api
from people.database import models

api = Api(
    title='People API',
    version='1.0',
    description='People related API'
)

api.add_namespace(people_api)
api.init_app(app)