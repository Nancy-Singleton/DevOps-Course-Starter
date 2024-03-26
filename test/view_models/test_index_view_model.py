from todo_app.models.item import Item
from todo_app.view_models.index_view_model import IndexViewModel

def test_done_items_property_returns_done_items():
    # arrange
    item_1 = Item(1, 'Completed item 1', 'Done')
    item_2 = Item(2, 'Completed item 2', 'Done')
    item_3 = Item(3, 'To do item 1', 'To Do')
    item_3 = Item(4, 'To do item 2', 'To Do')
    item_4 = Item(5, 'To do item 3', 'To Do')
    item_4 = Item(6, 'To do item 3', 'To Do')

    view_model = IndexViewModel([item_1, item_2, item_3, item_4])

    # act
    result = view_model.done_items

    # assert
    assert len(result) == 2