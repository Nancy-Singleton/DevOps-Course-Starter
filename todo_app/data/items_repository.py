import os
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


def get_items_collection():
    database_client = pymongo.MongoClient(os.getenv('CONNECTION_STRING'))
    database = database_client[os.getenv('DATABASE_NAME')]
    return database['to_do_items']
