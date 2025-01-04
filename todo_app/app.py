from flask import Flask, render_template, redirect, request
from loggly.handlers import HTTPSHandler
from logging import Formatter
from todo_app.data.items_repository import get_items, save_item, change_item_status

from todo_app.flask_config import Config
from todo_app.view_models.index_view_model import IndexViewModel

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())
    app.logger.setLevel(app.config['LOG_LEVEL'])

    if app.config['LOGGLY_TOKEN'] is not None:
        handler = HTTPSHandler(f'https://logs-01.loggly.com/inputs/{app.config["LOGGLY_TOKEN"]}/tag/todo-app')
        handler.setFormatter(
            Formatter("[%(asctime)s] %(levelname)s in %(module)s: %(message)s")
        )
        app.logger.addHandler(handler)

    @app.route('/')
    def index():
        items = get_items()
        item_view_model = IndexViewModel(items)

        app.logger.info("Homepage loaded")
        return render_template('index.html', view_model=item_view_model)

    @app.route('/item', methods=['POST'])
    def add_item():
        title = request.form.get('title')
        save_item(title)

        app.logger.info("Item added")
        return redirect('/')

    @app.route('/complete_item/<item_id>', methods=['POST'])
    def complete_item(item_id):
        change_item_status(item_id, "Done")

        app.logger.info("Item completed")
        return redirect('/')

    @app.route('/uncomplete_item/<item_id>', methods=['POST'])
    def uncomplete_item(item_id):
        change_item_status(item_id, "To Do")

        app.logger.info("Item uncompleted")
        return redirect('/')

    return app
