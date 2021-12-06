with open("input") as f:
    for l in f.readlines():
        l = l.strip()
        numbers = [int(x) for x in l.split(",")]

print(numbers)

by_nb = {}

for n in numbers:
    if n not in by_nb:
        by_nb[n] = 0
    by_nb[n] += 1


from collections import defaultdict

def it(by_nb):

    new_nbs = defaultdict(lambda: 0)

    for n, val in by_nb.items():

        if val:
            if n > 0:
                new_nbs[n - 1] += val
            else:
                new_nbs[6] += val
                new_nbs[8] += val

    return new_nbs

for x in range(0, 256):
    by_nb = it(by_nb)

print(sum(by_nb.values()))
