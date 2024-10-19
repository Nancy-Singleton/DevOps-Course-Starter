class Item:
    def __init__(self, id, name, status):
        self.id = id
        self.name = name
        self.status = status
    
    def is_to_do(self):
        return self.status == 'To Do'
              
    def is_doing(self):
        return self.status == 'Doing'
  
    def is_done(self):
        return self.status == 'Done'