# Running the App in Docker

## Prerequisites

- Follow the steps [here](shared-steps#mongo-db) to make sure you have a database available.
- Follow the steps [here](shared-steps#setting-up-env-file) to set up a `.env` file.

## Development Build

Run `docker compose -f docker/docker-compose-dev.yaml up --build`.

The app can then be accessed at `http://localhost:8080/`.

Changes made to your local code files should be reflected in the app without needing to rebuild the image.

## Production Build

Run `docker compose -f docker/docker-compose-prod.yaml up --build`.

The app can then be accessed at `http://localhost:8080/`.
