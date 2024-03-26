class IndexViewModel:
    def __init__(self, items):
        self._items = items
 
    @property
    def items(self):
        return self._items
    
    @property
    def done_items(self):
        return [x for x in self._items if x.is_done()]
    
    @property
    def doing_items(self):
        return []
    
    @property
    def to_do_items(self):
        return []