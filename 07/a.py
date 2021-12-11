with open("input") as f:
    for l in f.readlines():
        l = l.strip()
        crabs = [int(x) for x in l.split(",")]

minf = 9999999999
minmode = 0

for x in range(0, len(crabs)):
    cf = 0

    for c in crabs:
        for y in range(1, abs(c - x) + 1):
            cf += y #abs(c - x)

    if cf < minf:
        minf = cf
        minmode = x

print(minf, minmode)
