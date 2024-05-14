FROM python:3-buster as base

EXPOSE 5000
ENTRYPOINT root/.local/bin/poetry run flask run --host=0.0.0.0

RUN apt-get update 
RUN apt-get install -y curl
RUN curl -sSL https://install.python-poetry.org | python3 -

COPY pyproject.toml .
RUN root/.local/bin/poetry install

FROM base as production
COPY todo_app/ todo_app

FROM base as development