from .Automata import Automata

class Grudger(Automata):
    def __init__(self):
        super().__init__()
        self.name = "Grudger"
        self.is_opp_bad = False
    
    def move(self):
        return not self.is_opp_bad
    
    def observe(self, **kwargs):
        if kwargs["opp_move"] == False:
            self.is_opp_bad = True