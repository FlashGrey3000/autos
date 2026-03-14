from .Automata import Automata

class Evil(Automata):
    def __init__(self):
        self.name = "Evil"

    def move(self):
        return False