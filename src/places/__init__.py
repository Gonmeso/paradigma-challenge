from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restplus import Api
import places.config


app = Flask(__name__)
app.config.from_object(config.Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from places.v1.api import api as place_api
from places.database import models

api = Api(
    title='Place API',
    version='1.0',
    description='Place related API'
)

api.add_namespace(place_api)
api.init_app(app)