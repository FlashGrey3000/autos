from .Automata import Automata

class Perverse(Automata):
    def __init__(self):
        super().__init__()
        self.name = "Perverse"
        self.last_opp_move = True
    
    def move(self):
        return not self.last_opp_move
    
    def observe(self, **kwargs):
        self.last_opp_move = kwargs["opp_move"]