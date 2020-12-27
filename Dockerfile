FROM python:3.9

WORKDIR /code
COPY . /code/

RUN pip3 install pipenv
RUN pipenv install
