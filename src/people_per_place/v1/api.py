from flask import Flask
from flask_restplus import Resource, fields, Namespace
from .business import generate_response


api = Namespace('people-per-place', description = 'Places related operations')

people_fields = {
    'id': fields.String(description='Person identifier'),
    'name': fields.String(description='Person name'),
    'isAlive': fields.Boolean(
        description='Whether the person is dead or alive',
        attribute='isAlive'
    )
}

item_fields = {
    'id': fields.String(description='The place identifier'),
    'name': fields.String(description='The place name'),
    'people': fields.List(fields.Nested(people_fields))
}

all_people = api.model('all-people', {
    'items': fields.List(fields.Nested(item_fields))
})

people_per_place = api.model('people-per-place', item_fields)


@api.route('/')
class PeoplePerPlaceList(Resource):
    @api.doc('list_places_and_people')
    @api.marshal_list_with(all_people)
    def get(self):
        ''' List all places with their people'''
        response = generate_response()
        return response



@api.route('/<string:id>')
@api.param('id', 'The places identifier')
@api.response(404, 'Place not found')
class Place(Resource):
    @api.doc('get_people_per_place')
    @api.marshal_with(people_per_place)
    def get(self, id):
        ''' Fetch a place given its identifier'''
        response = generate_response(id)
        if response:
            return response
        api.abort(404)
