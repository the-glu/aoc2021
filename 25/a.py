m = {}

maxx = 0
maxy = 0

with open("input") as f:
    for x, l in enumerate(f.readlines()):
        l = l.strip()
        for y, v in enumerate(l):
            m[(x, y)] = v

            if maxy < y:
                maxy = y

        if maxx < x:
            maxx = x

def do_step_a(m):
    new_m = {}

    for x in range(0, maxx + 1):
        for y in range(0, maxy + 1):
            if m[(x, y)] == "v":
                dx = (x + 1) % (maxx + 1)
                if (dx, y) in m and m[(dx, y)] in [">", "v"]:
                    new_m[(x, y)] = "v"
                else:
                    new_m[(dx, y)] = "v"
            elif m[(x, y)] != ".":
                new_m[(x, y)] = m[(x, y)]

    for x in range(0, maxx + 1):
        for y in range(0, maxy + 1):
            if (x, y) not in new_m:
                new_m[(x, y)] = "."

    return new_m

def do_step_b(m):
    new_m = {}

    for x in range(0, maxx + 1):
        for y in range(0, maxy + 1):
            if m[(x, y)] == ">":
                dy = (y + 1) % (maxy + 1)
                if (x, dy) in m and m[(x, dy)]  in [">", "v"]:
                    new_m[(x, y)] = ">"
                else:
                    new_m[(x, dy)] = ">"
            elif m[(x, y)] != ".":
                new_m[(x, y)] = m[(x, y)]

    for x in range(0, maxx + 1):
        for y in range(0, maxy + 1):
            if (x, y) not in new_m:
                new_m[(x, y)] = "."

    return new_m


def disp():
    # return

    for x in range(0, maxx + 1):
        for y in range(0, maxy + 1):
            print(m.get((x, y), '.'), end="")
        print("")

disp()

nb_step = 0

while True:
    new_m = do_step_b(m)
    new_m = do_step_a(new_m)

    if new_m == m or False:
        m = new_m
        print(nb_step + 1)
        disp()
        print("")
        break
    nb_step += 1
    m = new_m
    # disp()
