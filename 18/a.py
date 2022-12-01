import math


def do_explode(l, level=0):

    if isinstance(l, int):
        return False, l, None, None

    l1, l2 = l

    if level >= 4:
        return True, 0, l1, l2

    exploded, new_l1, le, ri = do_explode(l1, level + 1)

    if exploded:

        def recuadd_left(ll):
            if isinstance(ll, int):
                return ll + ri
            else:
                return [recuadd_left(ll[0]), ll[1]]

        if ri:
            new_l2 = recuadd_left(l2)
            ri = None  # Already processed
        else:
            new_l2 = l2


    if exploded:
        return exploded, [new_l1, new_l2], le, ri

    exploded, new_l2, le, ri = do_explode(l2, level + 1)

    if exploded:

        def recuadd_right(ll):
            if isinstance(ll, int):
                return ll + le
            else:
                return [ll[0], recuadd_right(ll[1])]

        if le:
            new_l1 = recuadd_right(new_l1)
            le = None  # Already processed

    return exploded, [new_l1, new_l2], le, ri


def do_split(l):

    if isinstance(l, int):

        if l >= 10:
            return True, [math.floor(l / 2), math.ceil(l / 2)]
        return False, l

    l1, l2 = l

    splited, new_l1 = do_split(l1)

    if splited:
        return True, [new_l1, l2]

    splited, new_l2 = do_split(l2)

    return splited, [l1, new_l2]


def do_add(l1, l2):
    l = [l1, l2]

    done = False

    while not done:

        exploed, l, ri, le = do_explode(l)

        if not exploed:
            splited, l = do_split(l)

            if not splited:
                done = True

    return l




l = [[[[[9,8],1],2],3],4]
# l = [7,[6,[5,[4,[3,2]]]]]
# l = [[6,[5,[4,[3,2]]]],1]
# l = [[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]
# l = [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]
l = [[[[11,8],1],2],3]
l = [[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]

# print(do_explode(l))
# print(do_split(l))

x =[
    [1,1],
    [2,2],
    [3,3],
    [4,4],
    [5,5],
]

from inp import x


cl = x[0]

for xx in x[1:]:
    cl = do_add(cl, xx)
    print(cl)

def magn(l):
    if isinstance(l, int):
        return l
    return 3 * magn(l[0]) + 2 * magn(l[1])

print(magn(cl))

mx = 0
for x1 in x:
    for x2 in x:
        if x1 != x2:
            ma = magn(do_add(x1, x2))
            if ma > mx:
                mx = ma

print(mx)
