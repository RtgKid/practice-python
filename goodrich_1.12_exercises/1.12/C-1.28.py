import math


def norm(seq, n):
    return math.pow(sum([i ** n for i in seq]), 1 / n)


print(norm([3, 4], 2))
