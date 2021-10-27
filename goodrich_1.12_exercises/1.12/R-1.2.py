def is_even(k):
    return (k >> 1) + (k >> 1) == k


def is_even_better(k):
    return k & 1 == 0


print(is_even(7))
print(is_even(100))

print(is_even_better(7))
print(is_even_better(100))
