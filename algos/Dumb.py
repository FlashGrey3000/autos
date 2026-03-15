from .Automata import Automata
import random

class Dumb(Automata):
    def __init__(self):
        super().__init__()
        self.name = "Dumb"
    
    def move(self):
        return random.choice([True, False])
    
    def observe(self, **kwargs):
        pass