hp, de, aim = 0, 0, 0

with open("input") as f:
    for l in f.readlines():
        act, unit = l.split(" ")
        unit = int(unit)

        print(act, unit)

        if act == "forward":
            hp += unit
            de += aim * unit
        elif act == "down":
            # de += unit
            aim += unit
        elif act == "up":
            # de -= unit
            aim -= unit

        print(de, hp, aim)

print(hp, de, hp * de)
