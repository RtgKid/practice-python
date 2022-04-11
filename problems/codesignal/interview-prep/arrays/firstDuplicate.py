def solution(sequence):
    d = set()
    for i in sequence:
        if i in d:
            return i
        else:
            d.add(i)
    return -1   