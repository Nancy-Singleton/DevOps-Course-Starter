import os
import requests

def add_trello_item(title):
    """
    Adds a new item with the specified title to the Trello board.

    Args:
        title: The title of the item.
    """
    list_id = os.getenv('TRELLO_TO_DO_LIST_ID')
    key = os.getenv('TRELLO_API_KEY')
    token = os.getenv('TRELLO_API_TOKEN')
    
    url = f'https://api.trello.com/1/cards'
    params = {
        'idList': list_id,
        'key': key,
        'token': token
    }
    body = {'name': title}

    requests.post(url, body, params=params)

def complete_trello_item(item_id):
    """
    Moves the specified item to the "Done" list on the Trello board.

    Args:
        item_id: The id of the item.
    """
    done_list_id = os.getenv('TRELLO_DONE_LIST_ID')
    key = os.getenv('TRELLO_API_KEY')
    token = os.getenv('TRELLO_API_TOKEN')

    url=f'https://api.trello.com/1/cards/{item_id}'
    params = {
        'key': key,
        'token': token
    }
    body = {'idList': done_list_id}

    requests.put(url, body, params=params)