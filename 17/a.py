
txmi, txma, tymi, tyma = 20, 30, -10, -5

# target area: x=96..125, y=-144..-98

txmi, txma, tymi, tyma = 96, 125, -144, -98

def fire(vx, vy):
    x, y = (0, 0)
    maxy = -99999

    while x <= txma:
        x += vx
        y += vy

        maxy = max(y, maxy)

        if vx > 0:
            vx -= 1
        elif vx < 0:
            vx += 1

        vy -= 1

        if x >= txmi and x <= txma and y >= tymi and y <= tyma:
            return maxy

        if vx == 0 and (x < txmi or x > txma):
            return None

        if vx == 0 and vy < 0 and y < tymi:
            return None

    return None


mmmyy = -99999
ok = 0

for xx in range(0, 1000):
    for yy in range(-1000, 1000):
        r = fire(xx, yy)
        if r is not None:
            mmmyy = max(mmmyy, r)
            ok += 1

print(mmmyy, ok)
