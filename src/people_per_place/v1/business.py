import json
import requests


def list_places():
    response = requests.get('http://places-api:5000/places/')
    places = json.loads(response.text)

    return places


def get_place(id):
    response = requests.get(f'http://places-api:5000/places/{id}')
    place = json.loads(response.text)

    return place


def get_people():
    response = requests.get('http://people-api:5000/people/')
    people = json.loads(response.text)

    return people


def get_people_per_place(people, place_id):
    people_per_place = []
    for person in people:
        if 'placeId' in person.keys() and person['placeId'] == place_id:
            person.pop('placeId')
            people_per_place.append(person) 
    return people_per_place


def generate_response(id=None):
    response = {}
    people = get_people()
    if not id:
        items = []
        places = list_places()
        for place in places:
            item = {}
            item.update(place)
            item['people'] = get_people_per_place(people, place['id'])
            items.append(item)
        response['items'] = items
    else:
        response.update(get_place(id))
        response['people'] = get_people_per_place(people, id)
    return response
