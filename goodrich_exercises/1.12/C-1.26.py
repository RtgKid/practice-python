def foo(a, b, c):
    return a + b == c or a == b - c or a * b == c


print(foo(3, 100, 6))
print(foo(3, 5, 8))

