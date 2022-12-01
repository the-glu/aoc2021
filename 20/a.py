from collections import defaultdict
m = {}
maxx = 0
maxy = 0
minx = 0
miny = 0
baseline = ""

with open("input") as f:
    for x, l in enumerate(f.readlines()):
        l = l.strip()
        if not baseline:
            baseline = l
        else:
            for y, v in enumerate(l):
                m[(x - 1, y)] = v

                if maxy < y:
                    maxy = y

            if maxx < x - 1:
                maxx = x - 1

print(baseline, m)

def p(m):

    for x in range(minx, maxx + 1):
        for y in range(miny, maxy + 1):
            print(m.get((x, y)), end="")
        print("")

p(m)


def enhance(m, xxxx):
    new_m = {}

    global minx, miny, maxx, maxy

    minx -= 3
    miny -= 3
    maxx += 3
    maxy += 3

    for x in range(minx, maxx + 1):
        for y in range(miny, maxy + 1):

            n = ""

            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if (x + dx, y + dy) not in m:
                        n += "0" if xxxx % 2 == 0 else "1"
                    elif m[(x + dx, y + dy)] == "#":
                        n += "1"
                    else:
                        n += "0"
            pos = int(n, 2)
            new_m[(x, y)] = baseline[pos]


    return new_m

for x in range(0, 50):
    m = enhance(m, x)
    # p(m)
    print(x)

t = 0
for (x, y), v in m.items():

    if x > minx + 3 and x < maxx - 3:
        if y > miny + 3 and y < maxy - 3:
            if v == "#":
                t += 1
print(t)
