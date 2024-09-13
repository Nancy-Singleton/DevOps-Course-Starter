# Running the App in Docker

## Prerequisites

- Follow the steps [here](environment-variables) to configure environment variables.

## Development Build

Run `docker compose -f docker/docker-compose-dev.yaml up --build`.

The app can then be accessed at `http://localhost:8080/`.

Changes made to your local code files should be reflected in the app without needing to rebuild the image.

## Production Build

Run `docker compose -f docker/docker-compose-prod.yaml up --build`.

The app can then be accessed at `http://localhost:8080/`.
