from .Automata import Automata

class TitForTat(Automata):
    def __init__(self):
        super().__init__()
        self.name = "TitForTat"
        self.last_opp_move = True
    
    def move(self):
        return self.last_opp_move
    
    def observe(self, **kwargs):
        self.last_opp_move = kwargs["opp_move"]