import os
import requests

def get_items():
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
            cards.append({'id': card['id'], 'title': card['name'], 'status': list['name']})

    return cards