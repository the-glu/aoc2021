beacons = []

cb = []

with open("input") as f:
    for x, l in enumerate(f.readlines()):
        l = l.strip()

        if not l and cb:
            beacons.append(cb)
            cb = []
        elif "," in l:
            x, y, z = l.split(",")
            x, y, z = int(x), int(y), int(z)
            cb.append((x, y, z))

if cb:
    beacons.append(cb)

print(beacons)


def find_overlap(b1, b2):

    t = 0

    for swap in [0, 1, 2, 3, 4, 5]:
        for swap2 in [0]:

            for (ox, oy, oz) in [(1, 1, 1), (1, 1, -1), (1, -1, 1), (1, -1, -1), (-1, 1, 1), (-1, 1, -1), (-1, -1, 1), (-1, -1, -1)]:
                t += 1

                def s(b):
                    if swap == 0:
                        return b[0] * ox, b[1] * oy, b[2] * oz
                    elif swap == 1:
                        return b[2] * ox, b[1] * oy, b[0] * oz
                    elif swap == 2:
                        return b[1] * ox, b[2] * oy, b[0] * oz
                    elif swap == 3:
                        return b[1] * ox, b[0] * oy, b[2] * oz
                    elif swap == 4:
                        return b[2] * ox, b[0] * oy, b[1] * oz
                    else:
                        return b[0] * ox, b[2] * oy, b[1] * oz

                def s2(b):
                    if swap == 0:
                        return b[0], b[1], b[2]
                    elif swap == 1:
                        return b[2], b[1], b[0]
                    elif swap == 2:
                        return b[1], b[0], b[2]
                    else:
                        return b[0], b[2], b[1]

                def countmatch(new_b2, dx, dy, dz):
                    m = 0
                    for bb1 in b1:
                        # bb1 = s2(bb1)
                        for bb2 in new_b2:
                            # bb2 = s(bb2)
                            if bb1[0] + dx == bb2[0] and bb1[1] + dy == bb2[1] and bb1[2] + dz == bb2[2]:
                                m += 1
                    return m

                new_b2 = []
                for bb2 in b2:
                    new_b2.append(s(bb2))

                for bb1 in b1:
                    # bb1 = s2(bb1)

                    for bb2 in new_b2:
                        # bb2 = s(bb2)
                        dx, dy, dz = bb2[0] - bb1[0], bb2[1] - bb1[1], bb2[2] - bb1[2]

                        if countmatch(new_b2, dx, dy, dz) >= 12:

                            nnew_b2 = []
                            for bb2 in new_b2:
                                nnew_b2.append((bb2[0] - dx, bb2[1] - dy, bb2[2] - dz))

                            return dx, dy, dz, swap, ox, oy, oz, nnew_b2
                            return dx * ox, dy * oy, dz * oz

    # print(t)

found_pos = {0: (0, 0, 0), 9: (-1345, -6, -107), 21: (34, -85, 1193), 14: (3, 15, 2245), 23: (-89, -11, 3550), 1: (-4, 1098, 3554), 10: (27, -1299, 3572), 18: (-1202, -8, 3438), 24: (-71, -69, 4818), 25: (-117, 2299, 3519), 3: (36, -2485, 3558), 4: (-1224, -1325, 3545), 6: (-2395, -133, 3474), 11: (-1315, 31, 4751), 8: (-56, -67, 5949), 15: (1221, 26, 4764), 5: (-78, 2429, 2231), 2: (48, -2519, 2343), 22: (-95, -3646, 3433), 16: (-1310, -133, 6008), 12: (1085, 58, 5842), 26: (-147, 3613, 2366), 19: (-1324, -2484, 2397), 13: (31, -3683, 4764), 17: (-1340, 37, 7123), 20: (-1307, 1210, 5991), 7: (-123, -4828, 4691)}
# found_pos = {0: (0, 0, 0), 1: (-68, 1246, 43), 3: (92, 2380, 20), 4: (20, 1133, -1061), 2: (-1105, 1205, -1229)}
m = 0
print(found_pos)
for p1 in found_pos.values():
    for p2 in found_pos.values():
        md = abs(-p2[0] + p1[0]) + abs(-p2[1] + p1[1]) + abs(-p2[2] + p1[2])
        if md > m:
            m = md

print(m)

a = 1 / 0


found_pos = {0: (0, 0, 0)}

trucs_a_mapper = [(0, beacons[0])]
maping_done = {0: beacons[0]}

while trucs_a_mapper:
    pos, b1 = trucs_a_mapper.pop(0)

    for p2, b2 in enumerate(beacons):
        if p2 not in maping_done and p2 != pos:
            print("Trying to map", pos, p2)
            r = find_overlap(b1, b2)

            if r:
                dx, dy, dz, swap, ox, oy, oz, new_b2 = r
                print(r)
                trucs_a_mapper.append((p2, new_b2))
                maping_done[p2] = new_b2
                found_pos[p2] = dx, dy, dz

print(found_pos)

uniqueb = []

for _, v in maping_done.items():
    for b in v:
        if b not in uniqueb:
            uniqueb.append(b)

print(len(uniqueb))


# pairs = []
#
# for p1, b1 in enumerate(beacons):
#     for p2, b2 in enumerate(beacons):
#         if b1 != b2 and p1 < p2:
#             r = find_overlap(b1, b2)
#             print(p1, p2, r)
#             if r:
#                 pairs.append((p1, p2, r))
# pairs = [
# [0, 1, (-68, 1246, 43, 0, -1, 1, -1)],
# [1, 3, (-160, 1134, 23, 0, 1, 1, 1)],
# [1, 4, (-88, -113, 1104, 2, 1, -1, -1)],
# [2,4, (-1125, 168, -72, 3, 1, 1, -1)],
#
# ]
#
#
# for x in range(0, 10):
#     for p1, p2, r in pairs:
#         if p1 in found_pos and p2 not in found_pos:
#             p1x, p1y, p1z = found_pos[p1]
#             x, y, z, swap, ox, oy, oz = r
#             found_pos[p2] = p1x + x * 1, y * 1 + p1y, z * 1 + p1z
