import os
import requests

from todo_app.models.item import Item

def get_trello_items():
    """
    Fetches all saved items from the Trello board.

    Returns:
        list: The list of saved items.
    """
    board_id = os.getenv('TRELLO_BOARD_ID')
    key = os.getenv('TRELLO_API_KEY')
    token = os.getenv('TRELLO_API_TOKEN')
    trello_get_cards_url = f'https://api.trello.com/1/boards/{board_id}/lists?key={key}&token={token}&cards=open'

    response = requests.get(trello_get_cards_url)
    response_json = response.json()

    cards = []
    for list in response_json:
        for card in list['cards']:
            item = Item.from_trello_card(card, list)
            cards.append(item)

    return cards

def add_trello_item(title):
    """
    Adds a new item with the specified title to the Trello board.

    Args:
        title: The title of the item.
    """
    list_id = os.getenv('TRELLO_TO_DO_LIST_ID')
    key = os.getenv('TRELLO_API_KEY')
    token = os.getenv('TRELLO_API_TOKEN')
    
    url = f'https://api.trello.com/1/cards?idList={list_id}&key={key}&token={token}'
    body = {'name': title}

    requests.post(url, body)

def complete_trello_item(item_id):
    """
    Moves the specified item to the "Done" list on the Trello board.

    Args:
        item_id: The id of the item.
    """
    done_list_id = os.getenv('TRELLO_DONE_LIST_ID')
    key = os.getenv('TRELLO_API_KEY')
    token = os.getenv('TRELLO_API_TOKEN')

    url=f'https://api.trello.com/1/cards/{item_id}?key={key}&token={token}'
    body = {'idList': done_list_id}

    requests.put(url, body)