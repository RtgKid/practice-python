def compress(a:str) -> bool:
    s = list(a)
    res = []
    i = c = 0
    while i < len(s):
        if len(res) == 0:
            res.append(s[i])
        else:
            if s[i] == res[-1]:    
                c+=1
            else:
                res.append(str(c+1))
                c = 0
                res.append(s[i])
        i += 1
    if c != 0:
        res.append(str(c+1))
    result = ''.join(res)
    return len(s) == len(result)

print(compress("aabcccccaaa"))    