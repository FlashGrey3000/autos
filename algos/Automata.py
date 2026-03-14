class Automata:
    """Base automata class. Every automata must extend this class."""

    def __init__(self):
        pass
    
    def move(self, **kwargs):
        """returns a move for the round.  
        """
        raise NotImplementedError("Automata must implement the move() function.")