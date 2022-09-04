def string_rotation(s1: str, s2: str) -> bool:
    return s2 in s1+s1

print(string_rotation("waterbottle", "erbottlewat"))