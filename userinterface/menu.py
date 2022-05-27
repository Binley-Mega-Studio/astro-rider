class Menu_Button:
    def __init__(self, text, x, y, ):
        self.text = text
        self.x = x
        self.y = y
    

class Play_Button(Menu_Button):
    def __init__(self):
        super.__init__()

class Menu:
    def __init__(self):
        self.components = [Play_Button]
        
    def render(surface):
        pass
        
