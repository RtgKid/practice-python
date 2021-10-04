def factors(n):
    k = 1
    while k * k < n:
        if n % k == 0:
            yield k
            yield n // k
        k += 1
    if k * k == n:
        yield k


def factors_new(n):
    k = 1
    higher_factors = []
    while k * k < n:
        if n % k == 0:
            yield k
            higher_factors.append(n // k)
        k += 1
        if k * k == n:
            yield k
    for factor in reversed(higher_factors):
        yield factor


print([i for i in factors(100)])
print([i for i in factors_new(100)])
