def rotLeft(a, d):
    shifted = a[d%n:] + a[:d%n]
    return shifted