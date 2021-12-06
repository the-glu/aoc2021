gb, eb = "", ""

by_pos = [[], [], [], [], []]
by_pos = [[], [], [], [], [], [], [], [], [], [], [], []]

with open("input") as f:
    for l in f.readlines():

        for p, x in enumerate(l):
            if x in ["0", "1"]:
                by_pos[p].append(x)


import copy

by_pos2 = copy.deepcopy(by_pos)

for p in range(0, len(by_pos[0])):

    if len(by_pos[0]) > 1:

        nb_1 = len([x for x in by_pos[p] if x == "1"])

        lines_to_keep = []

        new_by_pos = [[], [], [], [], []]
        new_by_pos = [[], [], [], [], [], [], [], [], [], [], [], []]

        if nb_1 >= len(by_pos[0]) / 2:
            t = "1"
        else:
            t = "0"

        for subpos in range(0, len(by_pos)):
            for pp, pos in enumerate(by_pos[subpos]):
                if by_pos[p][pp] == t:
                    # print(by_pos, new_by_pos, pos, subpos)
                    new_by_pos[subpos].append(pos)

    print(by_pos, new_by_pos)
    by_pos = new_by_pos

print(by_pos)
gb = ''.join([x[0] for x in by_pos])
print(gb)

by_pos = by_pos2

for p in range(0, len(by_pos[0])):

    if len(by_pos[0]) > 1:

        nb_1 = len([x for x in by_pos[p] if x == "1"])

        lines_to_keep = []

        new_by_pos = [[], [], [], [], []]
        new_by_pos = [[], [], [], [], [], [], [], [], [], [], [], []]

        if nb_1 >= len(by_pos[0]) / 2:
            t = "0"
        else:
            t = "1"

        for subpos in range(0, len(by_pos)):
            for pp, pos in enumerate(by_pos[subpos]):
                if by_pos[p][pp] == t:
                    # print(by_pos, new_by_pos, pos, subpos)
                    new_by_pos[subpos].append(pos)

    print(by_pos, new_by_pos)
    by_pos = new_by_pos

print(by_pos)
eb = ''.join([x[0] for x in by_pos])
print(eb)


print(gb, eb)

gb = int(gb, 2)
eb = int(eb, 2)

print(gb, eb, gb * eb)
#
#
