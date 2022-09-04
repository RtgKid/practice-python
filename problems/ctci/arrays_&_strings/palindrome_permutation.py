def is_palindrome_permutation(s: str) -> bool:
    s = s.lower()
    d = {}
    odd_count = 0
    for i in s:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1      
    return sum(list(d.values())) % 2 != 0

print(is_palindrome_permutation('TactCoa'))    