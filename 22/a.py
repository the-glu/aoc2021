acts = []

with open("input") as f:
    for x, l in enumerate(f.readlines()):
        l = l.strip()

        act, ins = l.split(" ")
        x, y, z = ins.split(",")
        x1, x2 = x.split("..")
        y1, y2 = y.split("..")
        z1, z2 = z.split("..")
        x1, x2 = int(x1[2:]), int(x2)
        y1, y2 = int(y1[2:]), int(y2)
        z1, z2 = int(z1[2:]), int(z2)

        # x1, y1, z1 = max(x1, -50), max(y1, -50), max(z1, -50)
        # x2, y2, z2 = min(x2, 50), min(y2, 50), min(z2, 50)

        act = act == "on"

        acts.append((act, x1, x2, y1, y2, z1, z2))

from collections import defaultdict

c = defaultdict(lambda: False)


def inter(x1, x2, xx1, xx2):
    if x1 > x2 or xx1 > xx2:
        print("HOH")

    if x2 < xx1:
        return 1, 0
    if xx2 < x1:
        return 1, 0

    nx1 = min(max(xx1, x1), x2)
    nx2 = min(max(xx2, x1), x2)

    return nx1, nx2



def build_area(x1, x2, y1, y2, z1, z2, things_to_ignore):

    base_value = (x2 + 1 - x1) * (y2 + 1 - y1) * (z2 + 1 - z1)

    to_remove = []


    for __, xx1, xx2, yx1, yx2, zx1, zx2 in things_to_ignore:
        nx1, nx2 = inter(x1, x2, xx1, xx2)
        ny1, ny2 = inter(y1, y2, yx1, yx2)
        nz1, nz2 = inter(z1, z2, zx1, zx2)

        if (nx2-nx1 < 0) or (ny2 - ny1 < 0) or (nz2 - nz1 < 0):
            continue

        to_remove.append((False, nx1, nx2, ny1, ny2, nz1, nz2))

    while to_remove:
        __, nx1, nx2, ny1, ny2, nz1, nz2 = to_remove.pop(0)

        base_value -= build_area(nx1, nx2, ny1, ny2, nz1, nz2, to_remove)

    return base_value

t = 0

# acts = [
#     (True, 10, 12, 10, 12, 10, 12),
#     # (False, 9, 10, 9, 10, 9, 11),
# ]

while acts:
    act, x1, x2, y1, y2, z1, z2 = acts.pop(0)

    if act:
        t += build_area(x1, x2, y1, y2, z1, z2, acts)

    # if act:
    #     nb_on += (x2 + 1 - x1) * (y2 + 1 - y1) * (z2 + 1 - z2)


print(t)
