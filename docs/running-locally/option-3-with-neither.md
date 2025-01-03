# Prerequisites

- Install Python 3.8+
- Install [Poetry](https://python-poetry.org/docs/#system-requirements). This project uses poetry for Python to create an isolated environment and manage package dependencies.
- Check poetry is installed by running `poetry --version` from a terminal.
- Restart VSCode and any terminals you are running.
- Create the virtual environment and install required packages:

```bash
$ poetry install
```

- Follow the steps [here](shared-steps#mongo-db) to make sure you have a database available.
- Follow the steps [here](shared-steps#setting-up-env-file) to set up a `.env` file.

# Running the App

Start the Flask app in development mode within the Poetry environment by running:
```bash
$ poetry run flask --env-file env/.env run
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
