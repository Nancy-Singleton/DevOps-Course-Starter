# DevOps Apprenticeship: Project Exercise

> If you are using GitPod for the project exercise (i.e. you cannot use your local machine) then you'll want to launch a VM using the [following link](https://gitpod.io/#https://github.com/CorndelWithSoftwire/DevOps-Course-Starter). Note this VM comes pre-setup with Python & Poetry pre-installed.

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.8+ and install Poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

You can check poetry is installed by running `poetry --version` from a terminal.

**Please note that after installing poetry you may need to restart VSCode and any terminals you are running before poetry will be recognised.**

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/2.3.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie. There's also some `TRELLO_` variables which are covered in the [Trello Set Up](#trello-set-up) section below.

### Trello Set Up

The project uses a web service called Trello to store to-do items. To get the project running locally, you will need to:
* [Create a Trello account](https://trello.com/signup)
* [Generate an API key](https://developer.atlassian.com/cloud/trello/guides/rest-api/api-introduction/#managing-your-api-key) and use it to populate the `TRELLO_API_KEY` variable in the `.env` file
* Create an API token by clicking the link on the page where your API key is displayed, and use it to populate the `TRELLO_API_TOKEN` variable in the `.env` file
* Create a new board in your Trello account
* Follow [these instructions](https://developer.atlassian.com/cloud/trello/guides/rest-api/api-introduction/#your-first-api-call) to get the board ID, and use it to populate the `TRELLO_BOARD_ID` variable in the `.env` file
* Use [this endpoint](https://developer.atlassian.com/cloud/trello/rest/api-group-boards/#api-boards-id-lists-get) to get the list IDs for the board, and use them to populate the `TRELLO_<list name>_LIST_ID` variables in the `.env` file

## Running the App

Once the all dependencies have been installed, start the Flask app in development mode within the Poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app 'todo_app/app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 113-666-066
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

## Running the Tests
* The project uses [pytest](https://docs.pytest.org/en/stable/) to run unit tests.
* To run the tests from the command line, run `poetry run pytest`.
* To run in VSCode:
    * Run `Test: Refresh Tests` from the Command Palette.
    * You can then run or debug tests by:
        * Clicking the play button next to the test code
        * Navigating to the VSCode `Testing` tab

## Deploying the App

The app can be deployed to the hosts listed in the `inventory.yaml` file using the `playbook.yaml` Ansible playbook.

- Set up SSH access to each host.
- Run the following command.

```bash
$ ansible-playbook -i <inventory file> playbook.yaml
```

The app can then be accessed on port 5000 of each host.

## Running the App in Docker

### Production

Run `docker compose -f docker-compose-prod.yaml up --build`.

The app can then be accessed at `http://localhost:8080/`. 

### Development

Run `docker compose -f docker-compose-dev.yaml up --build`.

The app can then be accessed at `http://localhost:8080/`. 

Changes made to your local code files should be reflected in the app without needing to rebuild the image.

## Documentation

See [here](docs/docs.md) for documentation.