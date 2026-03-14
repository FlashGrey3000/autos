from .Automata import Automata

class Nice(Automata):
    def __init__(self):
        self.name = "Nice"

    def move(self):
        return True