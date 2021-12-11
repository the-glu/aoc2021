lines = []

mapping = {
    "0": "abcefg",
    "1": "cf",
    "2": "acdeg",
    "3": "acdfg",
    "4": "bcdf",
    "5": "abdfg",
    "6": "abdefg",
    "7": "acf",
    "8": "abcdefg",
    "9": "abcdfg",
}

with open("input") as f:
    for l in f.readlines():
        l = l.strip()
        l1, l2 = l.split(" | ")
        lines.append((l1.split(" "), l2.split(" ")))

import itertools

def make_sense(ll):

    for permu in itertools.permutations("abcdefg"):

        mapping2 = {
            permu[0]: "a",
            permu[1]: "b",
            permu[2]: "c",
            permu[3]: "d",
            permu[4]: "e",
            permu[5]: "f",
            permu[6]: "g",
        }

        def domap(x):
            r = []
            for xx in x:
                r.append(mapping2[xx])
            return ''.join(r)

        ok = True

        for l in ll:
            nb_match = 0
            tmatch = ""
            alltmach = []
            for k, v in mapping.items():
                if len(v) == len(l):
                    nb_match += 1
                    tmatch = v
                    alltmach.append(v)

            atleastoneok = False

            mapped = domap(l)
            if len(alltmach) == 1 or True:
                for ma in alltmach:
                    allcaraok = True
                    for x in mapped:
                        if x not in ma:
                            allcaraok = False
                            break
                    if allcaraok:
                        atleastoneok = True
                        break

                if not atleastoneok:
                    ok = False

        if ok:
            return mapping2
            print("ok", permu)

    print("------")


l1 = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab cdfeb fcadb cdfeb cdbaf".split(" ")
print(make_sense(l1))


count = 0

for l1, l2 in lines:
    for ll2 in l2:
        nb_match = 0
        for k, v in mapping.items():
            if len(v) == len(ll2):
                nb_match += 1

        if nb_match == 1:
            count += 1
t = 0
for l1, l2 in lines:
    permu = make_sense(l1 + l2)

    ftext = ""

    for digi in l2:

        r = []
        for xx in digi:
            r.append(permu[xx])
        dtext = ''.join(sorted(r))

        for k, v in mapping.items():
            if v == dtext:
                ftext = f"{ftext}{k}"

    print(ftext)
    t += int(ftext)



print(count, t)


