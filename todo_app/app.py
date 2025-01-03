from flask import Flask, render_template, redirect, request
from todo_app.data.items_repository import get_items, save_item, mark_item_done

from todo_app.flask_config import Config
from todo_app.view_models.index_view_model import IndexViewModel

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())

    @app.route('/')
    def index():
        items = get_items()
        item_view_model = IndexViewModel(items)
        return render_template('index.html', view_model=item_view_model)

    @app.route('/item', methods=['POST'])
    def add_item():
        title = request.form.get('title')
        save_item(title)
        return redirect('/')

    @app.route('/complete_item/<item_id>', methods=['POST'])
    def complete_item(item_id):
        mark_item_done(item_id)
        return redirect('/')

    return app
