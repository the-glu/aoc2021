poly = []

rules = {}

by_pair = {}

with open("input") as f:
    for x, l in enumerate(f.readlines()):
        l = l.strip()

        if not l:
            continue

        if not poly:
            poly = l
        else:
            fr, to = l.split(" -> ")
            rules[fr] = to


def do_a_step(p):

    new_p = ""

    for pos in range(0, len(p) - 1):
        fr = p[pos] + p[pos + 1]
        new_p += p[pos] + rules[fr]

    new_p += p[-1]

    return new_p


def do_a_step_v2(by_pair):
    by_pair_2 = {}

    for k, v in by_pair.items():
        rdest = rules[k]

        new_k = k[0] + rdest

        if new_k not in by_pair_2:
            by_pair_2[new_k] = 0

        by_pair_2[new_k] += v

        new_k = rdest + k[1]

        if new_k not in by_pair_2:
            by_pair_2[new_k] = 0

        by_pair_2[new_k] += v

    return by_pair_2


for pos in range(0, len(poly) - 1):
    key = poly[pos] + poly[pos + 1]
    if key not in by_pair:
        by_pair[key] = 0
    by_pair[key] += 1



for x in range(0, 40):
    print(by_pair)
    by_pair = do_a_step_v2(by_pair)


# for x in range(0, 40):
#     print(x)
#     poly = do_a_step(poly)

counters = {}

# for x in poly:
#     if x not in counters:
#         counters[x] = 0
#     counters[x] += 1
for k, v in by_pair.items():
    # if k[0] not in counters:
    #     counters[k[0]] = 0
    # counters[k[0]] += v
    if k[1] not in counters:
        counters[k[1]] = 0
    counters[k[1]] += v


l = list(sorted(counters.values()))
print(l[-1] - l[0])
