

lastd = 1
nbr = 0

def d():
    global lastd, nbr
    nbr += 1
    d = lastd
    lastd += 1
    if lastd > 100:
        lastd = 1
    return d

p1 = 2
p2 = 1
p1 = 4
p2 = 8
p1s = 0
p2s = 0

def w(p):
    while p > 10:
        p -= 10
    return p

while p1s <= 1000 and p2s <= 1000:

    p1 = w(p1 + d())
    p1 = w(p1 + d())
    p1 = w(p1 + d())

    p1s += p1

    if p1s >= 1000:
        break

    p2 = w(p2 + d())
    p2 = w(p2 + d())
    p2 = w(p2 + d())

    p2s += p2

    if p2s >= 1000:
        break

print(p1s, p2s, nbr, p1s * nbr, p2s * nbr)

cached_data = {}

def do_next_step(p1, p1s, p2, p2s, p1toplay=True):
    global cached_data
    k = f"{p1}_{p1s}_{p2}_{p2s}_{p1toplay}"
    if k in cached_data:
        return cached_data[k]

    p1w, p2w = 0, 0

    for d1 in [1, 2, 3]:
        for d2 in [1, 2, 3]:
            for d3 in [1, 2, 3]:
                if p1toplay:
                    nnp1 = w(p1 + d1 + d2 + d3)
                    np1s = p1s + nnp1

                    if np1s >= 21:
                        p1w += 1
                    else:
                        np1, np2 = do_next_step(nnp1, np1s, p2, p2s, False)
                        p1w += np1
                        p2w += np2
                else:
                    nnp2 = w(p2 + d1 + d2 + d3)
                    np2s = nnp2 + p2s

                    if np2s >= 21:
                        p2w += 1
                    else:
                        np1, np2 = do_next_step(p1, p1s, nnp2, np2s, True)
                        p1w += np1
                        p2w += np2

    cached_data[k] = p1w, p2w
    return p1w, p2w


print(do_next_step(2, 0, 1, 0, True))
