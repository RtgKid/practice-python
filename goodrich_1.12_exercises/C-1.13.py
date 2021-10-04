l = [1, 4, 5, 0, 58, 9]


def foo(n):
    rev_n = []
    for i in range(1, len(n) + 1):
        rev_n.append(n[-i])

    print(rev_n)


foo(l)