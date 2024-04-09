from todo_app.models.item import Item
from todo_app.view_models.index_view_model import IndexViewModel

def test_to_do_items_property_returns_to_do_items():
    # arrange
    items = create_items_with_statuses(['Done', 'Done', 'To Do', 'To Do', 'To Do', 'Doing'])
    view_model = IndexViewModel(items)

    # act
    result = view_model.to_do_items

    # assert
    assert len(result) == 3    

def test_doing_items_property_returns_doing_items():
    # arrange
    items = create_items_with_statuses(['Done', 'Done', 'To Do', 'To Do', 'To Do', 'Doing'])
    view_model = IndexViewModel(items)

    # act
    result = view_model.doing_items

    # assert
    assert len(result) == 1

def test_done_items_property_returns_done_items():
    # arrange
    items = create_items_with_statuses(['Done', 'Done', 'To Do', 'To Do', 'To Do', 'Doing'])
    view_model = IndexViewModel(items)

    # act
    result = view_model.done_items

    # assert
    assert len(result) == 2

def create_items_with_statuses(statuses):
    return [Item(idx + 1, 'An item description', status) for idx, status in enumerate(statuses)]