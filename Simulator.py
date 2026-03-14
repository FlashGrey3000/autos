from algos.Evil import Evil
from algos.Nice import Nice

table = {
    (True, True): (3,3),
    (True, False): (0,5),
    (False, True): (5,0),
    (False, False): (1,1)
    }

bot_a = Evil()
bot_b = Nice()

points_a, points_b = 0,0
for round in range(1, 101):
    move_a = bot_a.move()
    move_b = bot_b.move()

    rp_a, rp_b = table[(move_a, move_b)]

    points_a += rp_a
    points_b += rp_b

if points_b > points_a:
    print(f"{bot_b.name} wins with {points_b} points")
elif points_a > points_b:
    print(f"{bot_a.name} wins with {points_a} points")
else:
    print(f"Tie at {points_a} points")