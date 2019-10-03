from flask import Flask
from flask_restplus import Api
from people_per_place.v1.api import api as people_per_place_api


app = Flask(__name__)


api = Api(
    title='People per place API',
    version='1.0',
    description='Joins locations and people inside it API'
)

api.add_namespace(people_per_place_api)
api.init_app(app)