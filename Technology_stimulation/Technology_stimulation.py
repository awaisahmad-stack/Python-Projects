
#initial amount
robots = 10
drones = 6
stations = 50

day = 1

table = "-" * 50
table += "\n"
table += "Day".ljust(15)
table += 'Robots'.ljust(15)
table += "Drones".ljust(15)
table += "Stations".ljust(15)
table += "\n"
table += ("-" * 50)

while (robots > 0) and (drones > 0) and (stations > 0):
    stations *= 2


    if day % 2 == 0:

        if stations >= 4 * robots:
            stations -= robots * 4
            robots *= 2
        else:
            robots = 2 * (stations // 4)
            stations = stations % 4



    if day % 3 ==0:
        robots -= drones // 2
        if robots < 0:
            robots = 0

        if stations >= 3 * drones:
            stations -= 3 * drones
            drones *= 2

        else:
            drones = 2 * (stations // 3)
            stations = stations % 3


    if day % 4 == 0:
        robots -= 2 * (stations // 50)
        if robots < 0:
            robots = 0

        drones -= robots // 4
        if drones < 0:
            drones = 0

    table += "\n"
    table += str(day).ljust(15)
    table += str(robots).ljust(15)
    table += str(drones).ljust(15)
    table += str(stations).ljust(15)




    day += 1

print(table)

print("-" * 50)
