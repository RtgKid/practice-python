# Traditional way of implementing factors
def factors(n):
    results = []
    for k in range(1, n + 1):
        if n % k == 0:
            results.append(k)
    return results


print(factors(10))


# Now lets use generators
def factors_gen(n):
    for k in range(1, n + 1):
        if n % k == 0:
            yield k


print(factors_gen(10))

# Each iteration triggers the function till yield is reached
print([i for i in factors_gen(10)])


def fib():
    a = 0
    b = 1
    while True:
        yield a
        future = a + b
        a = b
        b = future


# Infinite series of fibonachi numbers
for i in fib():
    print(i)
