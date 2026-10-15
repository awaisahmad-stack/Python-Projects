import time

duration = 1
b1 = 100
b2 = 50
ca = 100


table = "-" * 50
table += "\n"
table += "Duration".ljust(15)
table += 'B1'.ljust(15)
table += "B2".ljust(15)
table += "CA".ljust(15)
table += "\n"
table += ("-" * 50)

while (b1 > 0 and b2 > 0) or (b1 > 0 and ca > 0) or ( b2 > 0 and ca > 0):
    ca *= 2

    if duration % 2 == 0:
        if ca >= 3 * b1:
            ca -= 3 * b1
            b1 *= 2
        else:
            b1 = 2 *(ca // 3)
            ca = ca % 3

    if duration % 3 == 0:
        b1 -= b2 // 2
        if b1 < 0:
            b1 = 0

        if ca >= 2 * b1:
            ca -= 2 * b1
            b1 *= 2
        else:
            b1 = 2 * (ca // 2)
            ca = ca % 2

    if duration % 4 == 0:
        b1 -= ca // 5
        b2 -= b1 // 3

        if b1 < 0:
            b1 = 0
        if b2 < 0:
            b2 = 0

    table += "\n"
    table += str(duration).ljust(15)
    table += str(b1).ljust(15)
    table += str(b2).ljust(15)
    table += str(ca).ljust(15)

    duration +=1
    time.sleep(0.3)

print(table)
