data = "D2FE28"
data = "FA0016C880162017C3686B18A3D4780"
data = "F805311100469800804A3E488ACC0B10055D8009548874F65665AD42F60073E7338E7E5C538D820114AEA1A19927797976F8F43CD7354D66747B3005B401397C6CBA2FCEEE7AACDECC017938B3F802E000854488F70FC401F8BD09E199005B3600BCBFEEE12FFBB84FC8466B515E92B79B1003C797AEBAF53917E99FF2E953D0D284359CA0CB80193D12B3005B4017968D77EB224B46BBF591E7BEBD2FA00100622B4ED64773D0CF7816600B68020000874718E715C0010D8AF1E61CC946FB99FC2C20098275EBC0109FA14CAEDC20EB8033389531AAB14C72162492DE33AE0118012C05EEB801C0054F880102007A01192C040E100ED20035DA8018402BE20099A0020CB801AE0049801E800DD10021E4002DC7D30046C0160004323E42C8EA200DC5A87D06250C50015097FB2CFC93A101006F532EB600849634912799EF7BF609270D0802B59876F004246941091A5040402C9BD4DF654967BFDE4A6432769CED4EC3C4F04C000A895B8E98013246A6016CB3CCC94C9144A03CFAB9002033E7B24A24016DD802933AFAE48EAA3335A632013BC401D8850863A8803D1C61447A00042E3647B83F313674009E6533E158C3351F94C9902803D35C869865D564690103004E74CB001F39BEFFAAD37DFF558C012D005A5A9E851D25F76DD88A5F4BC600ACB6E1322B004E5FE1F2FF0E3005EC017969EB7AE4D1A53D07B918C0B1802F088B2C810326215CCBB6BC140C0149EE87780233E0D298C33B008C52763C9C94BF8DC886504E1ECD4E75C7E4EA00284180371362C44320043E2EC258F24008747785D10C001039F80644F201217401500043A2244B8D200085C3F8690BA78F08018394079A7A996D200806647A49E249C675C0802609D66B004658BA7F1562500366279CCBEB2600ACCA6D802C00085C658BD1DC401A8EB136100"
# data = "F04005AC33890"

data = int(data, 16)
data = bin(data)
print(data)
data = str(data)[6:]
print(data)

ttvers = 0

def parse(d, finish=True):
    d = list(d)
    ver = int(d.pop(0) + d.pop(0) + d.pop(0), 2)
    typ = int(d.pop(0) + d.pop(0) + d.pop(0), 2)
    number = 0
    plength = 0
    pnumber = 0
    subpackets = []

    eat = 6

    if typ == 4:
        number = ""

        cont = True

        while cont:
            cont = d.pop(0) == "1"
            number += d.pop(0) + d.pop(0) + d.pop(0) + d.pop(0)
            eat += 5

        number = int(number, 2)

    else:
        i = d.pop(0)
        eat += 1

        if i == "0":
            plength = int(d.pop(0) + d.pop(0) + d.pop(0) + d.pop(0) + d.pop(0) + d.pop(0) + d.pop(0) + d.pop(0) + d.pop(0) + d.pop(0) + d.pop(0) + d.pop(0) + d.pop(0) + d.pop(0) + d.pop(0), 2)
            eat += 15
        else:
            pnumber = int(d.pop(0) + d.pop(0) + d.pop(0) + d.pop(0) + d.pop(0) + d.pop(0) + d.pop(0) + d.pop(0) + d.pop(0) + d.pop(0) + d.pop(0), 2)
            eat += 11

        if plength:
            toprocess = []
            for x in range(0, plength):
                toprocess.append(d.pop(0))
                eat += 1

            while toprocess:
                subp, toprocess = parse("".join(toprocess), False)
                subpackets.append(subp)
        else:
            print(pnumber)

            while len(subpackets) != pnumber:
                subp, d = parse("".join(d), False)
                subpackets.append(subp)

    if typ == 0:
        for subp in subpackets:
            number += subp[2]
    if typ == 1:
        number = subpackets[0][2]
        for subp in subpackets[1:]:
            number *= subp[2]
    if typ == 2:
        number = subpackets[0][2]
        for subp in subpackets[1:]:
            number = min(number, subp[2])
    if typ == 3:
        number = subpackets[0][2]
        for subp in subpackets[1:]:
            number = max(number, subp[2])
    if typ == 5:
        number = 1 if subpackets[0][2] > subpackets[1][2] else 0
    if typ == 6:
        number = 1 if subpackets[0][2] < subpackets[1][2] else 0
    if typ == 7:
        number = 1 if subpackets[0][2] == subpackets[1][2] else 0


    print(ver, typ, number, plength, pnumber, subpackets, d)
    global ttvers
    ttvers += ver
    return (ver, typ, number, plength, pnumber, subpackets), d

print(parse(data)[0][2])
