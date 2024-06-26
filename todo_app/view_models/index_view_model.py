class IndexViewModel:
    def __init__(self, items):
        self._items = items
 
    @property
    def items(self):
        return self._items

    @property
    def to_do_items(self):
        return [x for x in self._items if x.is_to_do()]

    @property
    def doing_items(self):
        return [x for x in self._items if x.is_doing()]

    @property
    def done_items(self):
        return [x for x in self._items if x.is_done()]
