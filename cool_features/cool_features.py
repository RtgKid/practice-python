# Packing
data = 3, 3, 5, 6
print(data)


def foo():
    return 4, 5


a = foo()
print(a)

a, b, c, d = range(0, 4)
print(c)

for x, y in [(1, 3), (2, 4)]:
    print(x, " : ", y)

# Assignments
x, y = 5, 6
print(x, y)

x, y = y, x
print(x, y)