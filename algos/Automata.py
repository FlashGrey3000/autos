class Automata:
    """Base automata class. Every automata must extend this class."""

    def __init__(self):
        pass
    
    def move(self):
        """returns a move for the round."""
        
        raise NotImplementedError("Automata must implement the move() function.")
    
    def observe(self, **kwargs):
        """observes the moves of this round.  

        **kwargs**: 
        - opp_move: bool
        - round_num: int
        - total_rounds: int
        - opp_name: str
        """
        raise NotImplementedError("Automata must implement observe() function")