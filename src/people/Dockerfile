FROM python:3.6-slim

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . /people
WORKDIR /people
CMD ["/bin/bash","start.sh"]