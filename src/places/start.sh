#!/bin/bash

sleep 60
flask db upgrade
python data/load_places.py
rm -rf data/
flask run --host=0.0.0.0