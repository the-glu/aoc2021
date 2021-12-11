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

tt = 0

bassins = []

for x in range(0, maxx + 1):
    for y in range(0, maxy + 1):
        ok = True

        for dx in [-1, 1]:
            if (x + dx, y) in m:
                if m[(x + dx, y)] <= m[(x, y)]:
                    ok = False

        for dy in [-1, 1]:
            if (x, y + dy) in m:
                if m[(x, y + dy)] <= m[(x, y)]:
                    ok = False
        if ok:
            tt += m[(x, y)] + 1

            to_check = [(x, y)]
            checked = []

            while to_check:
                cx, cy = to_check.pop(0)
                checked.append((cx, cy))

                for dx in [-1, 1]:
                    if (cx + dx, cy) in m and (cx + dx, cy) not in checked and (cx + dx, cy) not in to_check:
                        if m[(cx + dx, cy)] != 9:
                            to_check.append((cx + dx, cy))

                for dy in [-1, 1]:
                    if (cx, cy + dy) in m and (cx, cy + dy) not in checked and (cx, cy + dy) not in to_check:
                        if m[(cx, cy + dy)] != 9:
                            to_check.append((cx, cy + dy))

            bassins.append(len(checked))

print(bassins)

b = 1

for bb in sorted(bassins)[-3:]:
    b *= bb

print(b)

print(tt)
