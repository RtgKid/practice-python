#[0, 2, 6, 12, 20, 30, 42, 56, 72, 90].

def factors():
    a = 0
    factor = 0
    while True:
        yield a
        factor += 1
        a = a + 2*factor


gen = factors()
print([next(gen) for _ in range(10)])