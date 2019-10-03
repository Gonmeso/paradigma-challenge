import os
import pymysql
import random


DB_CONFIG = {
    'host': os.environ['DB_HOST'],
    'user': os.environ['DB_USER'],
    'password': os.environ['DB_PASSWORD'],
    'db': os.environ['DB_NAME'],
    'port': 3306
}

NUM_LOCATIONS = 26

def read_people():
    with open('data/people.csv') as csv:
        people = csv.readlines()
    return people


def clean_people(col):
    people = []
    for value in col:
        stripped = value.strip()
        if stripped not in people:
            people.append(stripped)
    return people


def random_is_alive():
    return bool(random.getrandbits(1))


def random_location(num_locations):
    return random.randrange(1, 26)


def insert_people(people):
    connection = pymysql.connect(**DB_CONFIG)
    with connection.cursor() as cursor:
        for person in people:
            liveness = random_is_alive()
            place = random_location(NUM_LOCATIONS)
            cursor.execute(
                f'''
                INSERT INTO people (name, is_alive, place_id)
                VALUES ("{person}", {liveness}, {place}) 
                '''
            )
            print(f'Inserting {person}, {liveness}, {place}')
        connection.commit()
        
    
def main():
    people = read_people()
    clean = clean_people(people)
    insert_people(clean)

if __name__ == '__main__':
    main()
