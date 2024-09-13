FROM python:3-buster as base


RUN apt-get update
RUN apt-get install -y curl
RUN curl -sSL https://install.python-poetry.org | python3 -

COPY ../todo_app todo_app

COPY ../pyproject.toml poetry.lock ./
RUN root/.local/bin/poetry install

FROM base as production
ENTRYPOINT root/.local/bin/poetry run flask run --host=0.0.0.0
EXPOSE 5000

FROM base as development
ENTRYPOINT root/.local/bin/poetry run flask run --host=0.0.0.0
EXPOSE 5000

FROM base as test
COPY ../test test
COPY ../env/.env.test env/
ENTRYPOINT root/.local/bin/poetry run pytest test
