m = {}

maxx = 0
maxy = 0

with open("input") as f:
    for x, l in enumerate(f.readlines()):
        l = l.strip()
        for y, v in enumerate(l):
            m[(x, y)] = int(v)

            if maxy < y:
                maxy = y

        if maxx < x:
            maxx = x

def disp():
    return

    for x in range(0, maxx + 1):
        for y in range(0, maxy + 1):
            print(m[(x, y)], end="")
        print("")

disp()
print()


for _ in range(1, 5):

    for x in range(0, maxx + 1):
        for y in range(0, maxy + 1):
            m[(x + (maxx + 1) * _, y)] = (m[(x + (maxx + 1) * (_ - 1), y)] + 1) % 10 or 1

maxx = (maxx + 1) * 5 - 1

disp()
print()

for _ in range(1, 5):

    for x in range(0, maxx + 1):
        for y in range(0, maxy + 1):
            m[(x, y + (maxy + 1) * _)] = (m[(x, y + (maxy + 1) * (_ - 1))] + 1) % 10 or 1

maxy = (maxy + 1) * 5 - 1

disp()


olist = []
clist = []

dists = {}
dists[(0, 0)] = 0

olist.append((0, 0))

i = 0

while olist:

    i += 1

    cpos = olist.pop(0)
    clist.append(cpos)
    x, y = cpos

    if cpos == (maxx, maxy):
        print(dists[cpos])
        break

    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:

            if (dx and not dy) or (not dx and dy):
                if (x + dx, y + dy) in m:

                    newd = dists[(x, y)] + m[(x + dx, y + dy)]

                    if (x + dx, y + dy) not in dists or newd < dists[(x + dx, y + dy)]:
                        dists[(x + dx, y + dy)] = newd

                        if (x + dx, y + dy) not in olist:
                            olist.append((x + dx, y + dy))

                        olist = sorted(olist, key=lambda xy: dists[xy])
