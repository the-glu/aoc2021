lines = []

with open("input") as f:
    for l in f.readlines():
        l = l.strip()
        lines.append(l)


def cor(c):
    if c == ")":
        return 3
    if c == "]":
        return 57
    if c == "}":
        return 1197
    if c == ">":
        return 25137

def sc(c):
    if c == "(":
        return 1
    if c == "[":
        return 2
    if c == "{":
        return 3
    if c == "<":
        return 4

tt = 0

scoooo = []
for line in lines:

    stack = []
    coru = 0

    for c in line:
        if c in ["[", "(", "<", "{"]:
            stack.append(c)
        else:
            carca = stack.pop(-1)

            if carca == "[" and c != "]":
                coru = cor(c)
                break

            if carca == "(" and c != ")":
                coru = cor(c)
                break

            if carca == "{" and c != "}":
                coru = cor(c)
                break

            if carca == "<" and c != ">":
                coru = cor(c)
                break

    if not coru:
        sco = 0

        for m in stack[::-1]:
            sco = sco * 5
            sco += sc(m)

        scoooo.append(sco)
        tt += sco

        print(line, coru, sco)
    # tt += coru

scoooo = sorted(scoooo)
print(scoooo[len(scoooo) // 2])

print(tt)

