from flask import Flask
from flask import render_template
from flask import request
from todo_app.data.session_items import add_item, get_items

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    items = get_items()
    
    return render_template('index.html', items = items)


@app.route('/item', methods=['POST']) 
def add_item_to_list():

    itemTitle = request.form.get('item-input')
    addItem = add_item(itemTitle)
    print(addItem)
    
    # return 
    return addItem
