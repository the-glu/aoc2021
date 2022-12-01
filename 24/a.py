ins = []


with open("input") as f:
    for x, l in enumerate(f.readlines()):
        l = l.strip()
        ins.append(l.split(" "))


def execute(n):
    global w, x, y, z
    w, x, y, z = 0, 0, 0, 0

    def getv(a):
        global w, x, y, z
        if a == "w":
            return w
        if a == "x":
            return x
        if a == "y":
            return y
        if a == "z":
            return z
        return int(a)

    def setv(a, v):
        global w, x, y, z
        if a == "w":
            w = v
        if a == "x":
            x = v
        if a == "y":
            y = v
        if a == "z":
            z = v

    for i in ins:

        if i[0] == "inp":
            # print(x, y, z, w)
            # setv(i[1], int(input("?")))
            setv(i[1], n.pop(0))
        elif i[0] == "add":
            setv(i[1], getv(i[1]) + getv(i[2]))
        elif i[0] == "mul":
            setv(i[1], getv(i[1]) * getv(i[2]))
        elif i[0] == "div":
            setv(i[1], int(getv(i[1]) // getv(i[2])))
        elif i[0] == "mod":
            setv(i[1], int(getv(i[1]) % getv(i[2])))
        elif i[0] == "eql":
            setv(i[1], 1 if getv(i[1]) == getv(i[2]) else 0)

    return z

# execute(1)
# print(x, y, z, w)

for n1 in [9]:
    for n2 in range(1, 10):
        for n3 in range(1, 10):
            n4 = n3 + 13 - 6
            if n4 > 0 and n4 < 10:
                for n5 in range(1, 10):
                    n6 = n5 - 4
                    if n6 > 0 and n6 < 10:
                        for n7 in [1]:
                            for n8 in range(1, 10):
                                for n9 in range(1, 10):
                                    n10 = n9 + 1
                                    if n10 > 0 and n10 < 10:
                                        n11 = n8 + 6
                                        if n11 > 0 and n11 < 10:
                                            for n12 in [9]:
                                                n13 = n2 + 7 - 9
                                                if n13 > 0 and n13 < 10:
                                                    for n14 in [1]:
                                                        if execute([n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13,n14]) == 0:
                                                            print(''.join([str(x) for x in [n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13,n14]]))
                                                            import sys
                                                            sys.exit(0)
