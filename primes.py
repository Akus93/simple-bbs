import random


def bigppr(bits=256):

    candidate = random.getrandbits(bits)
    if candidate & 1 == 0:
        candidate += 1
    prob = 0
    while 1:
        prob = pptest(candidate)
        if prob > 0:
            break
        else:
            candidate += 2
    return candidate


def pptest(n):

    bases = [random.randrange(2, 50000) for x in range(90)]
    if n <= 1:
        return 0
    for b in bases:
        if n % b == 0:
            return 0
    tests, s = 0, 0
    m = n-1

    while not m & 1:
        m >>= 1
        s += 1
    for b in bases:
        tests += 1
        isprob = algP(m, s, b, n)
        if not isprob:
            break

    if isprob:
        return 1-(1./(4**tests))
    else:
        return 0


def algP(m, s, b, n):
    result = 0
    y = pow(b, m, n)
    for j in range(s):
        if (y == 1 and j == 0) or (y == n - 1):
            result = 1
            break
        y = pow(y, 2, n)
    return result
