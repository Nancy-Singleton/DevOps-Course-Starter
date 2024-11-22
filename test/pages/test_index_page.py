import os
import pytest
from dotenv import load_dotenv, find_dotenv
from todo_app import app
import mongomock
import pymongo

@pytest.fixture
def client():
    file_path = find_dotenv('env/.env.test')
    load_dotenv(file_path, override=True)

    with mongomock.patch(servers=(('fakemongo.com', 27017),)):
        test_app = app.create_app()
        with test_app.test_client() as client:
            yield client

def test_index_page(client):
    # arrange
    set_up_data()

    # act
    response = client.get('/')

    # assert
    assert response.status_code == 200

    response_data = response.data.decode()
    assert 'Test Card' in response_data

def set_up_data():
    database_client = pymongo.MongoClient(os.getenv('CONNECTION_STRING'))
    database = database_client[os.getenv('DATABASE_NAME')]
    collection = database[os.getenv('ITEMS_COLLECTION_NAME')]
    collection.insert_one({"name": "Test Card", "status": "To Do"})
