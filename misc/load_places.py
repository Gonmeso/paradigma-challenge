import os
import pymysql


DB_CONFIG = {
    'host': os.environ['DB_HOST'],
    'user': os.environ['DB_USER'],
    'password': os.environ['DB_PASSWORD'],
    'db': os.environ['DB_NAME'],
    'port': 3306
}

def read_locations():
    with open('locations.csv') as csv:
        locations = csv.readlines()
    return locations


def clean_locations(col):
    locations = []
    for value in col:
        stripped = value.strip()
        if stripped not in locations:
            locations.append(stripped)
    return locations

def insert_locations(locations):
    connection = pymysql.connect(**DB_CONFIG)
    with connection.cursor() as cursor:
        for location in locations:
            cursor.execute(
                f'''
                INSERT INTO place (name)
                VALUES ("{location}") 
                '''
            )
        connection.commit()
        
    
def main():
    locations = read_locations()
    clean = clean_locations(locations)
    insert_locations(clean)
