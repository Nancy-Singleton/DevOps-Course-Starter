class Item:
    def __init__(self, id, name, status):
        self.id = id
        self.name = name
        self.status = status

    @classmethod
    def from_trello_card(cls, card, list):
        return cls(card['id'], card['name'], list['name'])
    
    def is_to_do(self):
        return self.status == 'To Do'
              
    def is_doing(self):
        return self.status == 'Doing'
  
    def is_done(self):
        return self.status == 'Done'