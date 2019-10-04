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