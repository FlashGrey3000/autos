from .Automata import Automata

class Evil(Automata):
    def __init__(self, **kwargs):
        self.name = "Evil"

    def move(self):
        return False
    
    def observe(self, **kwargs):
        pass