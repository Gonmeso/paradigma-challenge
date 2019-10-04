FROM python:3.6-slim

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . /people_per_place
WORKDIR /people_per_place
CMD ["flask", "run", "--host=0.0.0.0"]