from flask import Flask
from flask_restplus import Resource, fields, Namespace
from places.database.models import Place as Place_model


api = Namespace('places', description = 'Places related operations')

place = api.model('place', {
    'id': fields.String(description='The place identifier'),
    'name': fields.String(description='The place name'),
})


@api.route('/')
class PlaceList(Resource):
    @api.doc('list_places')
    @api.marshal_list_with(place)
    def get(self):
        ''' List all places'''
        places = Place_model.query.all()
        return places



@api.route('/<int:id>')
@api.param('id', 'The places identifier')
@api.response(404, 'Place not found')
class Place(Resource):
    @api.doc('get_place')
    @api.marshal_with(place)
    def get(self, id):
        ''' Fetch a place given its identifier'''
        place = Place_model.query.get(id)
        if place:
            return place
        api.abort(404)
