nb = 0
p = None

with open("input") as f:
    for l in f.readlines():
        l = int(l)

        if p is not None and l > p:
            nb += 1

        p = l

print(nb)


nb = 0
p = []
pm = 0

with open("input") as f:
    for l in f.readlines():
        l = int(l)

        if len(p) == 3:
            lm = (p[0] + p[1] + p[2]) / 3
            if lm > pm:
                nb += 1
            pm = lm
            p.pop(0)

        p.append(l)

print(nb)
