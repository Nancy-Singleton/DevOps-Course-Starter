FROM python:3-buster as base

ENTRYPOINT root/.local/bin/poetry run flask run --host=0.0.0.0

RUN apt-get update 
RUN apt-get install -y curl
RUN curl -sSL https://install.python-poetry.org | python3 -

COPY pyproject.toml poetry.lock ./
RUN root/.local/bin/poetry install

FROM base as production
COPY todo_app/ todo_app
EXPOSE 5000

FROM base as development
EXPOSE 5000