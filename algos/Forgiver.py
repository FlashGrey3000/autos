from .Automata import Automata

class Forgiver(Automata):
    def __init__(self):
        super().__init__()
        self.name = "Forgiver"
        self.betrayals = 0
    
    def move(self):
        if self.betrayals < 3:
            return True
        else:
            self.betrayals = 0
            return False
    
    def observe(self, **kwargs):
        if kwargs["opp_move"] == False:
            self.betrayals += 1
