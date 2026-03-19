from Simulator import Simulator

def main():
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


if __name__ == "__main__":
    main()
