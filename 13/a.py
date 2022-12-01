m = {}

maxx = 0
maxy = 0

ins = []

with open("input") as f:
    for x, l in enumerate(f.readlines()):
        l = l.strip()

        if not l:
            continue

        if "fold" in l:
            ___, inss = l.split("along ")

            ax, num = inss.split("=")

            ins.append((ax, int(num)))

        else:
            x, y = l.split(",")
            x, y = int(x), int(y)

            m[(x, y)] = True

            if maxy < y:
                maxy = y

            if maxx < x:
                maxx = x

def disp():

    ok = 0

    for y in range(0, maxy + 1):
        for x in range(0, maxx + 1):

            if m.get((x, y)):
                ok += 1
                print("#", end='')
            else:
                print(" ", end='')
        print("")


    print("----------------------", ok)
    print("----------------------")


def foldy(n):

    global maxy

    for y in range(0, n):
        for x in range(0, maxx + 1):
            if m.get((x, 2 * n - y)):
                m[(x, y)] = True

    maxy = n


def foldx(n):
    global maxx

    for x in range(0, n):
        for y in range(0, maxy + 1):
            if m.get((2 * n - x, y)):
                m[(x, y)] = True

    maxx = n



for ax, num in ins:
    # disp()

    if ax == "x":
        foldx(num)
    else:
        foldy(num)


disp()
