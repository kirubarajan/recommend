class Item:
    def __init__(self, id, text):
        self.text = text
        self.id = id
    
    def __str__(self):
        return str(self.id)