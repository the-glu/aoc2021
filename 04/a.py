import sys

numbers = []
pannels = []

cpannel = []

with open("input") as f:
    for l in f.readlines():
        l = l.strip()
        if not numbers:
            numbers = [int(x) for x in l.split(",")]
        else:
            if not l and cpannel:
                pannels.append(cpannel)
                cpannel = []
            elif l:
                cpannel.append([[int(x), False] for x in l.split(" ") if x])

pannels.append(cpannel)

print(numbers)
print(pannels)


def is_ok(p):

    def check_line(lid):
        for y in range(0, 5):
            if not p[lid][y][1]:
                return False

        return True

    def check_col(lid):
        for x in range(0, 5):
            if not p[x][lid][1]:
                return False

        return True

    for x in range(0, 5):
        if check_line(x):
            return True


    for y in range(0, 5):
        if check_col(y):
            return True

def pprintp(p):
    for x in range(0, 5):
        for y in range(0, 5):
            print(p[x][y], end=" ")
        print("")

boards_marks = []

for p in pannels:
    boards_marks.append(False)

for drawn in numbers:
    print("")
    print("")
    print(drawn)
    for ppos, p in enumerate(pannels):
        for x in range(0, 5):
            for y in range(0, 5):
                if p[x][y][0] == drawn:
                    p[x][y][1] = True

        if is_ok(p):
            boards_marks[ppos] = True

            if all(boards_marks):
                print("")
                print("")
                print("")
                pprintp(p)
                non_marked = 0
                for x in range(0, 5):
                    for y in range(0, 5):
                        if not p[x][y][1]:
                            non_marked += p[x][y][0]
                print(non_marked, non_marked * drawn)
                sys.exit(0)
        print("")
        pprintp(p)


