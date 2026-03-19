from init_db import getConnection

TABLE = {
    (True, True): (3,3),
    (True, False): (0,5),
    (False, True): (5,0),
    (False, False): (1,1)
    }

class Simulator:
    """Simulator class that simulates matches between two bots."""

    def __init__(self, bot_a, bot_b, num_rounds=100):
        self.bot_a = bot_a
        self.bot_b = bot_b
        self.points_a = 0
        self.points_b = 0
        self.num_rounds = num_rounds

        self.moves_a = []
        self.moves_b = []
        self.round_data = []
    
    def run(self):
        for r in range(1, self.num_rounds):
            move_a = self.bot_a.move()
            move_b = self.bot_b.move()

            rp_a, rp_b = TABLE[(move_a, move_b)]

            self.points_a += rp_a
            self.points_b += rp_b

            self.bot_a.observe(opp_move=move_b)
            self.bot_b.observe(opp_move=move_a)

            self.round_data.append((r, move_a, move_b, rp_a, rp_b))
        
        self.commit_data()
    
    def commit_data(self):
        conn = getConnection()
        curr = conn.cursor()

        bot_id_sql = ("SELECT * FROM automata")
        curr.execute(bot_id_sql)

        records = curr.fetchall()

        for record in records:
            if record[1] == self.bot_a.name:
                self.bot_a.id = record[0]

            if record[1] == self.bot_b.name:
                self.bot_b.id = record[0]
        
        
        match_sql = ("INSERT INTO matches"
                     "(automata_a, automata_b, points_a, points_b, winner)"
                     "VALUES (%s, %s, %s, %s, %s)"
                     "RETURNING id")
        
        if self.points_a > self.points_b:
            winner_id = self.bot_a.id
        elif self.points_a < self.points_b:
            winner_id = self.bot_b.id
        else:
            winner_id = -1

        curr.execute(match_sql, (self.bot_a.id, self.bot_b.id, self.points_a, self.points_b, winner_id))

        match_id = curr.fetchone()[0]

        record_sql = ("INSERT INTO rounds"
                      "(match_id, round, move_a, move_b, score_a, score_b)"
                      "VALUES (%s, %s, %s, %s, %s, %s)")
        
        curr.executemany(record_sql,
                         [(match_id, *x) for x in self.round_data])
        
        conn.commit()
        curr.close()
        conn.close()
    
    def results(self):
        if self.points_b > self.points_a:
            print(f"{self.bot_b.name} wins with {self.points_b} points")
        elif self.points_a > self.points_b:
            print(f"{self.bot_a.name} wins with {self.points_a} points")
        else:
            print(f"Tie at {self.points_a} points")
            


if __name__ == "__main__":
    from algos.Evil import Evil
    from algos.Nice import Nice
    from algos.BadTitForTat import BadTitForTat
    from algos.Dumb import Dumb
    from algos.Forgiver import Forgiver
    from algos.Grudger import Grudger
    from algos.Perverse import Perverse
    from algos.TitForTat import TitForTat

    autos = [Evil(), Nice(), BadTitForTat(), Dumb(), Forgiver(), Grudger(), Perverse(), TitForTat()]

    for bot_a in autos:
        for bot_b in autos:
            if bot_a.name == bot_b.name:
                continue
            sim = Simulator(bot_a=bot_a, bot_b=bot_b)

            sim.run()

            sim.results()