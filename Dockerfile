FROM python:3-buster

RUN apt-get update 
RUN apt-get install -y curl
RUN curl -sSL https://install.python-poetry.org | python3 -

COPY . .
RUN root/.local/bin/poetry install

ENTRYPOINT root/.local/bin/poetry run flask run --host=0.0.0.0
EXPOSE 5000