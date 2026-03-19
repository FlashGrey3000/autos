from config import load_configs
import psycopg2 as ps

def getConnection():
    configs = load_configs()

    conn = ps.connect(**configs)

    return conn

def create_tables():
    with getConnection() as conn:
        with conn.cursor() as curr:

            curr.execute("DROP TABLE IF EXISTS rounds, matches, automata;")

            curr.execute("""
                CREATE TABLE IF NOT EXISTS automata(
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(20) UNIQUE NOT NULL,
                        points INT
                        );
            """)

            curr.execute("""
                CREATE TABLE IF NOT EXISTS matches(
                        id SERIAL PRIMARY KEY,
                        automata_a INT NOT NULL,
                        automata_b INT NOT NULL,
                        points_a INT,
                        points_b INT,
                        winner INT,
                        FOREIGN KEY (automata_a) REFERENCES automata(id),
                        FOREIGN KEY (automata_b) REFERENCES automata(id),
                        FOREIGN KEY (winner) REFERENCES automata(id)
                        );
            """)

            curr.execute("""
                CREATE TABLE IF NOT EXISTS rounds(
                        match_id INT,
                        round INT,
                        move_a BOOLEAN,
                        move_b BOOLEAN,
                        score_a INT,
                        score_b INT,
                        PRIMARY KEY (match_id, round),
                        FOREIGN KEY (match_id) REFERENCES matches(id)
                        );
            """)

    print("Tables created successfully")

if __name__ == "__main__":
    with getConnection() as conn:
        with conn.cursor() as curr:

            print(conn.get_dsn_parameters())

            curr.execute("SELECT version();")

            print(curr.fetchone())

            create_tables()

            from algos.Evil import Evil
            from algos.Nice import Nice
            from algos.BadTitForTat import BadTitForTat
            from algos.Dumb import Dumb
            from algos.Forgiver import Forgiver
            from algos.Grudger import Grudger
            from algos.Perverse import Perverse
            from algos.TitForTat import TitForTat
            autos = [Evil(), Nice(), BadTitForTat(), Dumb(), Forgiver(), Grudger(), Perverse(), TitForTat()]

            init_auto_sql = ("INSERT INTO automata"
                            "(name, points)"
                            "VALUES (%s, %s);")
            
            curr.execute("INSERT INTO automata VALUES (%s, %s, %s)",
                        (-1, "Tie", 0))

            curr.executemany(init_auto_sql,
                            [(a.name, 0) for a in autos])