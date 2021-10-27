def foo(seq):
    return any([seq[i] == seq[j] for i in range(len(seq)) for j in range(len(seq)) if i != j])


print(foo([1, 3, 5, 6, 2, 1]))
print(foo([1, 3, 5, 6, 2]))


def scale(data, factor):
    for j in range(len(data)):
        data[j] *= factor


def new_scale(data, factor):
    for j in data:
        j *= factor


a = [1, 3]
new_scale(a, 2)
print(a)
