# Repository regarding *[Paradigma](https://github.com/paradigmadigital/python-challenge)* python challenge


The main purpose of the challenge is to create thre microservices that allows to get information from Game of Thrones characters. These microservices retrieve the following information:

* GoT places (or locations): retrieves the name of the location and a unique identifier

```
[
    {
        "id": 1,
        "name": "Descaro del Rey"
    },
    {
        "id": 2,
        "name": "Más allá del Zumo"
    },
    {
        "id": 3,
        "name": "Veranolandia"
    }
]
```

* GoT characters information regarding, location (identifier), name, identifier and whether the character is alive or not

```
[
    {
        "id": 1,
        "name": "Sensei Lamister",
        "isAlive": true,
        "placeId": 1
        
    },
    {
        "id": 2,
        "name": "Aiba Stack",
        "isAlive": true,
        "placeId": 3
    }
]
```

* A join between the previous information

```
[
    {
        "id": 1,
        "name": "Descaro del Rey",
        "people": [
            {
                "id": 1,
                "name": "Sensei Lamister",
                "isAlive": true
            }, {
                "id": 5,
                "name": "Juanito Lamister",
                "isAlive": true
            }
        ]
    },
    {
        "id": 2,
        "name": "Más allá del Zumo",
        "people": [
            {
                "id": 3,
                "name": "Juaquín Nevado",
                "isAlive": true
            }
        ]
    }
]
```

### Constraints

* The first two microservices must have their own database
* Use flask/flask-restplus
* Use SQLAlchemy for data retrieval
* Use Alembic for DB migrations/creation
* Use synthetic data
* Document how to run the code
* Unit tests

Rergarding the constraints, the Alembic one is halfway done, the creation of the DB is made using the MySQL docker environment variables, that allow the creation of a database at start up. But migrations are made using flask-migrate (Alembic) and commited to the repo.

*ATM* no unit tests have been made but they are a TODO (using pytest) and POST, DELETES and UPDATES are not implemented (next sprint :P)

### Nice to have´s

* Dockerize all three microservices

From the start the application has been developed having in mind the dockerization of services, and a docker-compose is provided in order to deploy them.

### How to run the code

To run the microservices (and the databases) `docker` and `docker-compose` are needed. Furthermore, some environment files are needed for the main two microservices, one for the database and one por the api,  so four in total:

**Database**

```
MYSQL_ROOT_PASSWORD=  
MYSQL_ROOT_HOST=%      # Allow external connections
MYSQL_DATABASE=        # Name of the database to create on startup
MYSQL_USER=            # User for the database
MYSQL_PASSWORD=        # Password fot the database
```

**Api**

```
DATABASE_URI=mysql+pymysql://{user}:{password}@{host}:{port}/{db_name}
DB_HOST=        # Same values as in the database env file
DB_USER=        # Same values as in the database env file
DB_PASSWORD=    # Same values as in the database env file
DB_NAME=        # Same values as in the database env file
```

In order to deploy the services the next steps must be followed:

1. Clone the repo

`git clone https://github.com/Gonmeso/paradigma-challenge.git`

2. Change directory into the repo folder

`cd paradigma-challenge`

3. Execute docker-compose

`docker-compose up -d`

Once the services are deployed the next ports are mapped:

* MySQL 1: 3306
* MySQL 2: 3307
* Microservice places: 5001
* Microservice people: 5002
* Microservice people-per-place: 5003

### Examples

**Places**

```
>>> r = requests.get('http://localhost:5001/places/')
>>> pprint.pprint(json.loads(r.text))

[{'id': '1', 'name': 'Golden Tooth'},
 {'id': '2', 'name': "Mummer's Ford"},
 {'id': '3', 'name': "Torrhen's Square"},
 {'id': '4', 'name': 'Winterfell'},
 {'id': '5', 'name': 'Oxcross'},
 {'id': '6', 'name': "Storm's End"},
 {'id': '7', 'name': 'Red Fork'},
 {'id': '8', 'name': 'Harrenhal'},
 {'id': '9', 'name': 'Crag'},
 {'id': '10', 'name': "King's Landing"},
 ```

 ```
>>> r = requests.get('http://localhost:5001/places/1')
>>> pprint.pprint(json.loads(r.text))

{'id': '1', 'name': 'Golden Tooth'}
```

**People**

```
>>> r = requests.get('http://localhost:5002/people/')
>>> pprint.pprint(json.loads(r.text))
[{'id': '1', 'isAlive': 'True', 'name': 'Viserys Plumm', 'placeId': '15'},
 {'id': '2', 'isAlive': 'True', 'name': 'Melissa Blackwood', 'placeId': '7'},
 {'id': '3', 'isAlive': 'True', 'name': 'Larys Strong', 'placeId': '19'},
 {'id': '4', 'isAlive': 'False', 'name': 'Nettles', 'placeId': '7'},
 {'id': '5', 'isAlive': 'True', 'name': 'Baela Targaryen', 'placeId': '12'},
 {'id': '6',
  'isAlive': 'False',
  'name': 'Daella Targaryen (daughter of Maekar I)',
  'placeId': '5'}]
```

```
>>> r = requests.get('http://localhost:5002/people/1')
>>> pprint.pprint(json.loads(r.text))
{'id': '1', 'isAlive': 'True', 'name': 'Viserys Plumm', 'placeId': '15'}
```

**People-per-place**

```
>>> r = requests.get('http://localhost:5003/people-per-place/')
>>> pprint.pprint(json.loads(r.text))
{'items': [{'id': '1',
            'name': 'Golden Tooth',
            'people': [{'id': '38',
                        'isAlive': True,
                        'name': 'Daenerys Targaryen (daughter of Aegon IV)'}]},
           {'id': '2',
            'name': "Mummer's Ford",
            'people': [{'id': '7', 'isAlive': False, 'name': 'Daena Targaryen'},
                       {'id': '13',
                        'isAlive': False,
                        'name': 'Saera Targaryen'},
                       {'id': '14', 'isAlive': True, 'name': 'Barba Bracken'},
                       {'id': '19',
                        'isAlive': False,
                        'name': 'Aegon Targaryen (son of Jaehaerys I)'}]},
           {'id': '3',
            'name': "Torrhen's Square",
            'people': [{'id': '21',
                        'isAlive': True,
                        'name': 'Rhaegel Targaryen'},
                       {'id': '27',
                        'isAlive': False,
                        'name': 'Rhaenys Targaryen'}]}]
}
```

```
>>> r = requests.get('http://localhost:5003/people-per-place/24')
>>> pprint.pprint(json.loads(r.text))
{'id': '24',
 'name': 'Dragonstone',
 'people': [{'id': '12', 'isAlive': True, 'name': 'Medger Cerwyn'},
            {'id': '36',
             'isAlive': False,
             'name': 'Rhaena Targaryen (daughter of Daemon)'},
            {'id': '37', 'isAlive': False, 'name': 'Corlys Velaryon'}]}
```

### Folder structure

The proyect follows the next structure across microservices

```
src
└── microservice
    ├── Dockerfile
    ├── __init__.py
    ├── app.py
    ├── config.py
    ├── data                        # Only fot loading synthetic data
    │   ├── load_*.py
    │   └── data.csv
    ├── database                    # SQL Alchemy 
    │   ├── __init__.py
    │   └── models.py
    ├── migrations                  # Alembic
    │   ├── README
    │   ├── alembic.ini
    │   ├── env.py
    │   ├── script.py.mako
    │   └── versions
    │       └── a7f47eb3a536.py
    ├── requirements.txt            # Docker requirements
    ├── start.sh                    # Entrypoint for the container (if needed)
    └── v1                          # Api version
        ├── __init__.py
        └── api.py
```

Lastly, I want to thank Paradigma for such entertaining challenge that pushed me to use (and most importanly, learn) Flask, SQLAlchemy, Alembic and API development overall, had a great time learning the frameworks.