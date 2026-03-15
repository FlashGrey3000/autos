from .Automata import Automata

class BadTitForTat(Automata):
    def __init__(self):
        super().__init__()
        self.name = "BadTitForTat"
        self.last_opp_move = False
    
    def move(self):
        return self.last_opp_move
    
    def observe(self, **kwargs):
        self.last_opp_move = kwargs["opp_move"]