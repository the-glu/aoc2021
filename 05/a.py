from collections import defaultdict

lines = []


with open("input") as f:
    for l in f.readlines():
        l = l.strip()

        fr, to = l.split(" -> ")
        x1, y1 = fr.split(",")
        x2, y2 = to.split(",")
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

        lines.append((x1, y1, x2, y2))

print(lines)


bigmap = defaultdict(lambda: 0)

for x1, y1, x2, y2 in lines:

    if x1 == x2 or y1 == y2:
        if x1 == x2:
            if y2 < y1:
                y1, y2 = y2, y1
            for y in range(y1, y2 + 1):
                bigmap[(x1, y)] += 1
        else:
            if x2 < x1:
                x1, x2 = x2, x1
            for x in range(x1, x2 + 1):
                bigmap[(x, y1)] += 1
    else:
        if x2 < x1:
            for delta, x in enumerate(range(x1, x2 - 1, -1)):
                if y2 < y1:
                    delta = -delta
                bigmap[(x, y1 + delta)] += 1
        else:
            for delta, x in enumerate(range(x1, x2 + 1)):
                if y2 < y1:
                    delta = -delta
                bigmap[(x, y1 + delta)] += 1


t = 0
for v in bigmap.values():
    if v > 1:
        t += 1

print(bigmap, t)
