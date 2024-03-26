from flask import Flask, render_template, redirect, request
from todo_app.data.trello_items import get_trello_items, add_trello_item, complete_trello_item

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    items = get_trello_items()
    return render_template('index.html', items = items)

@app.route('/item', methods=['POST'])
def add_item():
    title = request.form.get('title')
    add_trello_item(title)
    return redirect('/')

@app.route('/complete_item/<item_id>', methods=['POST'])
def complete_item(item_id):
    complete_trello_item(item_id)
    return redirect('/')