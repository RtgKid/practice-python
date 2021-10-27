def foo(seq):
    return any([i * j for i in seq for j in seq if i != j and i*j & 1 == 1])


print(foo([1, 3, 2, 6, 10]))
print(foo([3, 2, 6, 10]))