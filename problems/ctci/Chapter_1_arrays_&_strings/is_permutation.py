def is_permutation(s1:str, s2:str) -> bool:
    d = {}
    for i in s1:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    for i in s2:
        if i not in d:
            return False
        else:
            d[i] -=1

    return sum(d.values()) == 0


print(is_permutation("abcdef", "ebdfac"))                           
print(is_permutation("abcdefk", "ebdfaco"))