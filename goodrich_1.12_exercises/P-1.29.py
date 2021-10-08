# c a t d o g

def foo(data):
    if len(data) == 1:
        return data

    elif len(data) == 2:
        return [data[1] + data[0], data[0] + data[1]]

    else:
        print(data[1:])
        return merge(data[0], foo(data[1:]))


def merge(el, l):
    result = []
    for word in l:
        for i in range(len(word) + 1):
            result.append(word[:i] + el + word[i:])

    return result


print(foo("catdog"))