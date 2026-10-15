
#initial amount
hunters = 6
wolves = 8
sheep = 12
day = 1
table = ("-" * 50)
table += "\n"
table += "Day".ljust(15)
table += 'Hunter'.ljust(15)
table += "Sheep".ljust(15)
table += "Wolves".ljust(15)
table += "\n"
table += ("-" * 50)


while (hunters > 0) and (wolves > 0) and (sheep > 0):
    sheep += sheep // 5

    if day % 2 == 0:
        trios = wolves // 3
        wolves -= wolves % 3

        if sheep >= trios:
            sheep -= trios
            wolves += trios

        else:
            trios_sur = sheep
            sheep = 0
            trios_die = trios - trios_sur
            wolves -= trios_die * 3
            wolves += trios_sur

        hunters += 1

    if day % 3 == 0:
        wolves -= hunters // 2
        if wolves < 0:
            wolves = 0

        pairs = wolves // 2
        wolves -= wolves % 2

        if sheep >= pairs:
            sheep -= pairs
            wolves += pairs
        else:
            pairs_sur = sheep
            sheep = 0
            pairs_die = pairs - pairs_sur
            wolves -= pairs_die * 2
            wolves += pairs_sur

    if day % 4 == 0:
        wolves -= sheep // 30
        if wolves < 0:
            wolves = 0

        hunters -= wolves // 10
        if hunters < 0:
            hunters = 0

    table += "\n"
    table += str(day).ljust(15)
    table += str(hunters).ljust(15)
    table += str(sheep).ljust(15)
    table += str(wolves).ljust(15)

    day += 1

print(table)