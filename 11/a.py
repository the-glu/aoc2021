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

nb_flash = 0
for r in range(0, 1000000):

    for k, v in m.items():
        m[k] = v + 1

    flashed = []
    done = False

    while not done:
        done = True

        for x in range(0, maxx + 1):
            for y in range(0, maxy + 1):
                if m[(x, y)] > 9 and (x, y) not in flashed:
                    flashed.append((x, y))

                    done = False

                    for dx in [-1, 0, 1]:
                        for dy in [-1, 0, 1]:
                            if (x + dx, y + dy) in m:
                                m[(x + dx, y + dy)] += 1


    nb_flash += len(flashed)
    if len(flashed) == len(m.keys()):
        print(r + 1)
        break

    for p in flashed:
        m[p] = 0

print(m)

print(nb_flash)
