from flask import Flask
from flask_restplus import Resource, fields, Namespace
from people.database.models import People as People_model


api = Namespace('people', description = 'People related operations')

people = api.model('people', {
    'id': fields.String(description='The person identifier'),
    'name': fields.String(description='The person name'),
    'isAlive': fields.String(
        description='Whether the person is alive or not',
        attribute='is_alive',
    ),
    'placeId': fields.String(
        description='Id of the persons related place',
        attribute='place_id',
    ),
})


@api.route('/')
class PeopleList(Resource):
    @api.doc('list_people')
    @api.marshal_list_with(people)
    def get(self):
        ''' List all places'''
        people = People_model.query.all()
        return people



@api.route('/<int:id>')
@api.param('id', 'The character/person identifier')
@api.response(404, 'Character not found')
class Person(Resource):
    @api.doc('get_person')
    @api.marshal_with(people)
    def get(self, id):
        ''' Fetch a person given its identifier'''
        person = People_model.query.get(id)
        if person:
            return person
        api.abort(404)
