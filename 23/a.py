
hallway = [None] * 11
slot1 = ['B', 'D', 'D', 'A']
slot2 = ['C', 'C', 'B', 'D']
slot3 = ['B', 'B', 'A', 'C']
slot4 = ['D', 'A', 'C', 'A']

slot1 = ['A', 'D', 'D', 'B']
slot2 = ['C', 'C', 'B', 'A']
slot3 = ['B', 'B', 'A', 'D']
slot4 = ['D', 'A', 'C', 'C']

def basec(x):
    if x == 'A':
        return 1
    elif x == 'B':
        return 10
    elif x == 'C':
        return 100
    else:
        return 1000

def canigotoslot(x, slots, spos):
    if x == 'A' and spos != 1:
        return -1
    if x == 'B' and spos != 2:
        return -1
    if x == 'C' and spos != 3:
        return -1
    if x == 'D' and spos != 4:
        return -1

    if slots[3] is None:
        return 3
    elif slots[3] == x and slots[2] is None:
        return 2
    elif slots[3] == x and slots[2] == x and slots[1] is None:
        return 1
    elif slots[3] == x and slots[2] == x and slots[1] == x and slots[0] is None:
        return 0

    return -1


def possible_moves(situation):
    hallway, slot1, slot2, slot3, slot4 = situation

    # slots to hallway
    for slotpos in range(0, 4):
        if slot1[slotpos]:

            need_to_move = False

            for sspos in range(slotpos, 4):
                if slot1[sspos] != 'A':
                    need_to_move = True

            if need_to_move:

                baseslot = slot1[slotpos]
                nslot1 = slot1[::]
                nslot1[slotpos] = None

                if not hallway[1]:
                    nhallway = hallway[::]
                    nhallway[1] = baseslot
                    yield nhallway, nslot1, slot2, slot3, slot4, basec(baseslot) * (2 + slotpos)

                    if not hallway[0]:
                        nhallway = hallway[::]
                        nhallway[0] = baseslot
                        yield nhallway, nslot1, slot2, slot3, slot4, basec(baseslot) * (3 + slotpos)

                if not hallway[3]:
                    nhallway = hallway[::]
                    nhallway[3] = baseslot
                    yield nhallway, nslot1, slot2, slot3, slot4, basec(baseslot) * (2 + slotpos)

                    c = canigotoslot(baseslot, slot2, 2)

                    if c != -1:
                        nslot2 = slot2[::]
                        nslot2[c] = baseslot
                        yield hallway, nslot1, nslot2, slot3, slot4, basec(baseslot) * (4 + c + slotpos)

                    if not hallway[4] and not hallway[5]:
                        nhallway = hallway[::]
                        nhallway[5] = baseslot
                        yield nhallway, nslot1, slot2, slot3, slot4, basec(baseslot) * (4 + slotpos)

                        c = canigotoslot(baseslot, slot3, 3)

                        if c != -1:
                            nslot3 = slot3[::]
                            nslot3[c] = baseslot
                            yield hallway, nslot1, slot2, nslot3, slot4, basec(baseslot) * (6 + c + slotpos)

                        if not hallway[6] and not hallway[7]:
                            nhallway = hallway[::]
                            nhallway[7] = baseslot
                            yield nhallway, nslot1, slot2, slot3, slot4, basec(baseslot) * (6 + slotpos)

                            c = canigotoslot(baseslot, slot4, 4)

                            if c != -1:
                                nslot4 = slot4[::]
                                nslot4[c] = baseslot
                                yield hallway, nslot1, slot2, slot3, nslot4, basec(baseslot) * (8 + c + slotpos)

                            if not hallway[8] and not hallway[9]:
                                nhallway = hallway[::]
                                nhallway[9] = baseslot
                                yield nhallway, nslot1, slot2, slot3, slot4, basec(baseslot) * (8 + slotpos)

                                if not hallway[10]:
                                    nhallway = hallway[::]
                                    nhallway[10] = baseslot
                                yield nhallway, nslot1, slot2, slot3, slot4, basec(baseslot) * (9 + slotpos)

            break

    for slotpos in range(0, 4):
        if slot2[slotpos]:

            need_to_move = False

            for sspos in range(slotpos, 4):
                if slot2[sspos] != 'B':
                    need_to_move = True

            if need_to_move:

                baseslot = slot2[slotpos]
                nslot2 = slot2[::]
                nslot2[slotpos] = None

                if not hallway[3]:
                    nhallway = hallway[::]
                    nhallway[3] = baseslot
                    yield nhallway, slot1, nslot2, slot3, slot4, basec(baseslot) * (2 + slotpos)

                    c = canigotoslot(baseslot, slot1, 1)

                    if c != -1:
                        nslot1 = slot1[::]
                        nslot1[c] = baseslot
                        yield hallway, nslot1, nslot2, slot3, slot4, basec(baseslot) * (4 + c + slotpos)

                    if not hallway[2] and not hallway[1]:
                        nhallway = hallway[::]
                        nhallway[1] = baseslot
                        yield nhallway, slot1, nslot2, slot3, slot4, basec(baseslot) * (4 + slotpos)

                        if not hallway[0]:
                            nhallway = hallway[::]
                            nhallway[0] = baseslot
                            yield nhallway, slot1, nslot2, slot3, slot4, basec(baseslot) * (5 + slotpos)

                if not hallway[5]:
                    nhallway = hallway[::]
                    nhallway[5] = baseslot
                    yield nhallway, slot1, nslot2, slot3, slot4, basec(baseslot) * (2 + slotpos)

                    c = canigotoslot(baseslot, slot3, 3)

                    if c != -1:
                        nslot3 = slot3[::]
                        nslot3[c] = baseslot
                        yield hallway, slot1, nslot2, nslot3, slot4, basec(baseslot) * (4 + c + slotpos)

                    if not hallway[6] and not hallway[7]:
                        nhallway = hallway[::]
                        nhallway[7] = baseslot
                        yield nhallway, slot1, nslot2, slot3, slot4, basec(baseslot) * (4 + slotpos)

                        c = canigotoslot(baseslot, slot4, 4)

                        if c != -1:
                            nslot4 = slot4[::]
                            nslot4[c] = baseslot
                            yield hallway, slot1, nslot2, slot3, nslot4, basec(baseslot) * (6 + c + slotpos)

                        if not hallway[8] and not hallway[9]:
                            nhallway = hallway[::]
                            nhallway[9] = baseslot
                            yield nhallway, slot1, nslot2, slot3, slot4, basec(baseslot) * (6 + slotpos)

                            if not hallway[10]:
                                nhallway = hallway[::]
                                nhallway[10] = baseslot
                                yield nhallway, slot1, nslot2, slot3, slot4, basec(baseslot) * (7 + slotpos)


            break

    for slotpos in range(0, 4):
        if slot3[slotpos]:

            need_to_move = False

            for sspos in range(slotpos, 4):
                if slot3[sspos] != 'C':
                    need_to_move = True

            if need_to_move:

                baseslot = slot3[slotpos]
                nslot3 = slot3[::]
                nslot3[slotpos] = None

                if not hallway[5]:
                    nhallway = hallway[::]
                    nhallway[5] = baseslot
                    yield nhallway, slot1, slot2, nslot3, slot4, basec(baseslot) * (2 + slotpos)

                    c = canigotoslot(baseslot, slot2, 2)

                    if c != -1:
                        nslot2 = slot2[::]
                        nslot2[c] = baseslot
                        yield hallway, slot1, nslot2, nslot3, slot4, basec(baseslot) * (4 + c + slotpos)

                    if not hallway[4] and not hallway[3]:
                        nhallway = hallway[::]
                        nhallway[3] = baseslot
                        yield nhallway, slot1, slot2, nslot3, slot4, basec(baseslot) * (4 + slotpos)

                        c = canigotoslot(baseslot, slot1, 1)

                        if c != -1:
                            nslot1 = slot1[::]
                            nslot1[c] = baseslot
                            yield hallway, nslot1, slot2, nslot3, slot4, basec(baseslot) * (6 + c + slotpos)

                        if not hallway[2] and not hallway[1]:
                            nhallway = hallway[::]
                            nhallway[1] = baseslot
                            yield nhallway, slot1, slot2, nslot3, slot4, basec(baseslot) * (6 + slotpos)

                            if not hallway[0]:
                                nhallway = hallway[::]
                                nhallway[0] = baseslot
                                yield nhallway, slot1, slot2, nslot3, slot4, basec(baseslot) * (7 + slotpos)

                if not hallway[7]:
                    nhallway = hallway[::]
                    nhallway[7] = baseslot
                    yield nhallway, slot1, slot2, nslot3, slot4, basec(baseslot) * (2 + slotpos)

                    c = canigotoslot(baseslot, slot4, 4)

                    if c != -1:
                        nslot4 = slot4[::]
                        nslot4[c] = baseslot
                        yield hallway, slot1, slot2, nslot3, nslot4, basec(baseslot) * (4 + c + slotpos)

                    if not hallway[8] and not hallway[9]:
                        nhallway = hallway[::]
                        nhallway[9] = baseslot
                        yield nhallway, slot1, slot2, nslot3, slot4, basec(baseslot) * (4 + slotpos)

                        if not hallway[10]:
                            nhallway = hallway[::]
                            nhallway[10] = baseslot
                            yield nhallway, slot1, slot2, nslot3, slot4, basec(baseslot) * (5 + slotpos)

            break

    for slotpos in range(0, 4):
        if slot4[slotpos]:

            need_to_move = False

            for sspos in range(slotpos, 4):
                if slot4[sspos] != 'D':
                    need_to_move = True

            if need_to_move:

                baseslot = slot4[slotpos]
                nslot4 = slot4[::]
                nslot4[slotpos] = None

                if not hallway[7]:
                    nhallway = hallway[::]
                    nhallway[7] = baseslot
                    yield nhallway, slot1, slot2, slot3, nslot4, basec(baseslot) * (2 + slotpos)

                    c = canigotoslot(baseslot, slot3, 3)

                    if c != -1:
                        nslot3 = slot3[::]
                        nslot3[c] = baseslot
                        yield hallway, slot1, slot2, nslot3, nslot4, basec(baseslot) * (4 + c + slotpos)

                    if not hallway[6] and not hallway[5]:
                        nhallway = hallway[::]
                        nhallway[5] = baseslot
                        yield nhallway, slot1, slot2, slot3, nslot4, basec(baseslot) * (4 + slotpos)

                        c = canigotoslot(baseslot, slot2, 2)

                        if c != -1:
                            nslot2 = slot2[::]
                            nslot2[c] = baseslot
                            yield hallway, slot1, nslot2, slot3, nslot4, basec(baseslot) * (6 + c + slotpos)

                        if not hallway[4] and not hallway[3]:
                            nhallway = hallway[::]
                            nhallway[3] = baseslot
                            yield nhallway, slot1, slot2, slot3, nslot4, basec(baseslot) * (6 + slotpos)

                            c = canigotoslot(baseslot, slot1, 1)

                            if c != -1:
                                nslot1 = slot1[::]
                                nslot1[c] = baseslot
                                yield hallway, nslot1, slot2, slot3, nslot4, basec(baseslot) * (8 + c + slotpos)

                            if not hallway[2] and not hallway[1]:
                                nhallway = hallway[::]
                                nhallway[1] = baseslot
                                yield nhallway, slot1, slot2, slot3, nslot4, basec(baseslot) * (8 + slotpos)

                                if not hallway[0]:
                                    nhallway = hallway[::]
                                    nhallway[0] = baseslot
                                    yield nhallway, slot1, slot2, slot3, nslot4, basec(baseslot) * (9 + slotpos)

                if not hallway[9]:
                    nhallway = hallway[::]
                    nhallway[9] = baseslot
                    yield nhallway, slot1, slot2, slot3, nslot4, basec(baseslot) * (2 + slotpos)

                    if not hallway[10]:
                        nhallway = hallway[::]
                        nhallway[10] = baseslot
                        yield nhallway, slot1, slot2, slot3, nslot4, basec(baseslot) * (3 + slotpos)


            break

    # hallway to slots
    if hallway[0]:

        baseslot = hallway[0]
        nhallway = hallway[::]
        nhallway[0] = None

        if not hallway[1] and not hallway[2]:
            c = canigotoslot(baseslot, slot1, 1)

            if c != -1:
                nslot1 = slot1[::]
                nslot1[c] = baseslot
                yield nhallway, nslot1, slot2, slot3, slot4, basec(baseslot) * (3 + c)

            if not hallway[3] and not hallway[4]:
                c = canigotoslot(baseslot, slot2, 2)

                if c != -1:
                    nslot2 = slot2[::]
                    nslot2[c] = baseslot
                    yield nhallway, slot1, nslot2, slot3, slot4, basec(baseslot) * (5 + c)

                if not hallway[5] and not hallway[6]:
                    c = canigotoslot(baseslot, slot3, 3)

                    if c != -1:
                        nslot3 = slot3[::]
                        nslot3[c] = baseslot
                        yield nhallway, slot1, slot2, nslot3, slot4, basec(baseslot) * (7 + c)

                    if not hallway[7] and not hallway[8]:
                        c = canigotoslot(baseslot, slot4, 4)

                        if c != -1:
                            nslot4 = slot4[::]
                            nslot4[c] = baseslot
                            yield nhallway, slot1, slot2, slot3, nslot4, basec(baseslot) * (9 + c)

    if hallway[1]:

        baseslot = hallway[1]
        nhallway = hallway[::]
        nhallway[1] = None

        if not hallway[2]:
            c = canigotoslot(baseslot, slot1, 1)

            if c != -1:
                nslot1 = slot1[::]
                nslot1[c] = baseslot
                yield nhallway, nslot1, slot2, slot3, slot4, basec(baseslot) * (2 + c)

            if not hallway[3] and not hallway[4]:
                c = canigotoslot(baseslot, slot2, 2)

                if c != -1:
                    nslot2 = slot2[::]
                    nslot2[c] = baseslot
                    yield nhallway, slot1, nslot2, slot3, slot4, basec(baseslot) * (4 + c)

                if not hallway[5] and not hallway[6]:
                    c = canigotoslot(baseslot, slot3, 3)

                    if c != -1:
                        nslot3 = slot3[::]
                        nslot3[c] = baseslot
                        yield nhallway, slot1, slot2, nslot3, slot4, basec(baseslot) * (6 + c)

                    if not hallway[7] and not hallway[8]:
                        c = canigotoslot(baseslot, slot4, 4)

                        if c != -1:
                            nslot4 = slot4[::]
                            nslot4[c] = baseslot
                            yield nhallway, slot1, slot2, slot3, nslot4, basec(baseslot) * (8 + c)

    if hallway[3]:

        baseslot = hallway[3]
        nhallway = hallway[::]
        nhallway[3] = None

        c = canigotoslot(baseslot, slot1, 1)

        if c != -1:
            nslot1 = slot1[::]
            nslot1[c] = baseslot
            yield nhallway, nslot1, slot2, slot3, slot4, basec(baseslot) * (2 + c)

        c = canigotoslot(baseslot, slot2, 2)

        if c != -1:
            nslot2 = slot2[::]
            nslot2[c] = baseslot
            yield nhallway, slot1, nslot2, slot3, slot4, basec(baseslot) * (2 + c)

        if not hallway[5] and not hallway[6]:
            c = canigotoslot(baseslot, slot3, 3)

            if c != -1:
                nslot3 = slot3[::]
                nslot3[c] = baseslot
                yield nhallway, slot1, slot2, nslot3, slot4, basec(baseslot) * (4 + c)

            if not hallway[7] and not hallway[8]:
                c = canigotoslot(baseslot, slot4, 4)

                if c != -1:
                    nslot4 = slot4[::]
                    nslot4[c] = baseslot
                    yield nhallway, slot1, slot2, slot3, nslot4, basec(baseslot) * (6 + c)

    if hallway[5]:

        baseslot = hallway[5]
        nhallway = hallway[::]
        nhallway[5] = None

        if not hallway[3]:
            c = canigotoslot(baseslot, slot1, 1)

            if c != -1:
                nslot1 = slot1[::]
                nslot1[c] = baseslot
                yield nhallway, nslot1, slot2, slot3, slot4, basec(baseslot) * (4 + c)

        c = canigotoslot(baseslot, slot2, 2)

        if c != -1:
            nslot2 = slot2[::]
            nslot2[c] = baseslot
            yield nhallway, slot1, nslot2, slot3, slot4, basec(baseslot) * (2 + c)

        c = canigotoslot(baseslot, slot3, 3)

        if c != -1:
            nslot3 = slot3[::]
            nslot3[c] = baseslot
            yield nhallway, slot1, slot2, nslot3, slot4, basec(baseslot) * (2 + c)

        if not hallway[7] and not hallway[8]:
            c = canigotoslot(baseslot, slot4, 4)

            if c != -1:
                nslot4 = slot4[::]
                nslot4[c] = baseslot
                yield nhallway, slot1, slot2, slot3, nslot4, basec(baseslot) * (4 + c)

    if hallway[7]:

        baseslot = hallway[7]
        nhallway = hallway[::]
        nhallway[7] = None

        if not hallway[5]:
            c = canigotoslot(baseslot, slot2, 2)

            if c != -1:
                nslot2 = slot2[::]
                nslot2[c] = baseslot
                yield nhallway, slot1, nslot2, slot3, slot4, basec(baseslot) * (4 + c)

            if not hallway[3]:
                c = canigotoslot(baseslot, slot1, 1)

                if c != -1:
                    nslot1 = slot1[::]
                    nslot1[c] = baseslot
                    yield nhallway, nslot1, slot2, slot3, slot4, basec(baseslot) * (6 + c)

        c = canigotoslot(baseslot, slot3, 3)

        if c != -1:
            nslot3 = slot3[::]
            nslot3[c] = baseslot
            yield nhallway, slot1, slot2, nslot3, slot4, basec(baseslot) * (2 + c)

        c = canigotoslot(baseslot, slot4, 4)

        if c != -1:
            nslot4 = slot4[::]
            nslot4[c] = baseslot
            yield nhallway, slot1, slot2, slot3, nslot4, basec(baseslot) * (2 + c)

    if hallway[9]:

        baseslot = hallway[9]
        nhallway = hallway[::]
        nhallway[9] = None

        if not hallway[7]:

            c = canigotoslot(baseslot, slot3, 3)

            if c != -1:
                nslot3 = slot3[::]
                nslot3[c] = baseslot
                yield nhallway, slot1, slot2, nslot3, slot4, basec(baseslot) * (4 + c)

            if not hallway[5]:
                c = canigotoslot(baseslot, slot2, 2)

                if c != -1:
                    nslot2 = slot2[::]
                    nslot2[c] = baseslot
                    yield nhallway, slot1, nslot2, slot3, slot4, basec(baseslot) * (6 + c)

                if not hallway[3]:
                    c = canigotoslot(baseslot, slot1, 1)

                    if c != -1:
                        nslot1 = slot1[::]
                        nslot1[c] = baseslot
                        yield nhallway, nslot1, slot2, slot3, slot4, basec(baseslot) * (8 + c)

        c = canigotoslot(baseslot, slot4, 4)

        if c != -1:
            nslot4 = slot4[::]
            nslot4[c] = baseslot
            yield nhallway, slot1, slot2, slot3, nslot4, basec(baseslot) * (2 + c)

    if hallway[10] and not hallway[9]:

        baseslot = hallway[10]
        nhallway = hallway[::]
        nhallway[10] = None

        if not hallway[7]:

            c = canigotoslot(baseslot, slot3, 3)

            if c != -1:
                nslot3 = slot3[::]
                nslot3[c] = baseslot
                yield nhallway, slot1, slot2, nslot3, slot4, basec(baseslot) * (5 + c)

            if not hallway[5]:
                c = canigotoslot(baseslot, slot2, 2)

                if c != -1:
                    nslot2 = slot2[::]
                    nslot2[c] = baseslot
                    yield nhallway, slot1, nslot2, slot3, slot4, basec(baseslot) * (7 + c)

                if not hallway[3]:
                    c = canigotoslot(baseslot, slot1, 1)

                    if c != -1:
                        nslot1 = slot1[::]
                        nslot1[c] = baseslot
                        yield nhallway, nslot1, slot2, slot3, slot4, basec(baseslot) * (9 + c)

        c = canigotoslot(baseslot, slot4, 4)

        if c != -1:
            nslot4 = slot4[::]
            nslot4[c] = baseslot
            yield nhallway, slot1, slot2, slot3, nslot4, basec(baseslot) * (3 + c)

olist = []
clist = []
dists = {}


situation = (hallway, slot1, slot2, slot3, slot4)

def skey(situation):
    return str(situation)

dists[skey(situation)] = 0
olist.append((situation, 0))

while olist:

    csituation, cdist = olist.pop(0)
    # clist.append(skey(situation))

    # cdist = dists[skey(csituation)]
    # print(csituation, cdist)

    print(len(olist), cdist)

    if csituation[1] == ['A', 'A', 'A', 'A'] and csituation[2] == ['B', 'B', 'B', 'B'] and csituation[3] == ['C', 'C', 'C', 'C'] and csituation[4] == ['D', 'D', 'D', 'D']:
        print(cdist)
        break

    for h, s1, s2, s3, s4, distannce in possible_moves(csituation):
        nsit = h, s1, s2, s3, s4

        newd = cdist + distannce
        nkey = skey(nsit)

        if nkey not in dists or newd < dists[nkey]:

            dists[nkey] = newd
            olist.append((nsit, newd))

            olist = sorted(olist, key=lambda x: x[1])

# for x in possible_moves():
#     print(x)

