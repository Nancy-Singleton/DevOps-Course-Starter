import os
from bson import ObjectId
import pymongo

from todo_app.models.item import Item

def get_items():
    """
    Fetches all saved items.

    Returns:
        list: The list of saved items.
    """
    db_records = get_items_collection().find()
    items = []
    for record in db_records:
        id = str(record.get('_id'))
        item = Item(id, record.get('name'), record.get('status'))
        items.append(item)
    return items

def save_item(title):
    """
    Creates a new item with the specified title.

    Args:
        title: The title of the item.
    """
    db_collection = get_items_collection()
    db_collection.insert_one({"name": title, "status": "To Do"})

def mark_item_done(item_id):
    """
    Updates the status of the specified item to "Done".

    Args:
        item_id: The id of the item.
    """
    db_collection = get_items_collection()
    db_collection.update_one({'_id': ObjectId(item_id)}, { "$set": { "status": "Done" } })


def get_items_collection():
    database_client = pymongo.MongoClient(os.getenv('CONNECTION_STRING'))
    database = database_client[os.getenv('DATABASE_NAME')]
    return database['to_do_items']
