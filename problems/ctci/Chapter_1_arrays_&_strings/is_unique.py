def is_unique(s : str) -> bool:
    d = {}
    for i in s:
        if i in d:
            return False
        else:
            d[i] = 1
    return True 


def is_unique2(s: str) -> bool:
    sorted_s = sorted(s)
    for i in range(len(s) - 1):
        if sorted_s[i] == sorted_s[i+1]:
            return False
    return True        


print(is_unique('blabla'))
print(is_unique('qwerty'))


print(is_unique2('blabla'))
print(is_unique2('qwerty'))