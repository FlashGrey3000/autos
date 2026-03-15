from .Automata import Automata

class Nice(Automata):
    def __init__(self, **kwargs):
        self.name = "Nice"

    def move(self):
        return True
    
    def observe(self, **kwargs):
        pass