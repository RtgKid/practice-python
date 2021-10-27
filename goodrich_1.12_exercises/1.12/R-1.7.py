def foo(n):
    return sum([i * i for i in range(n) if i & 1 == 1])


print(foo(6))