from flask import Flask, render_template, redirect, request
from todo_app.data.trello_items import get_items, add_item

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    items = get_items()
    return render_template('index.html', items = items)

@app.route('/item', methods=['POST'])
def new_item():
    title = request.form.get('title')
    add_item(title)
    return redirect('/')