def solution(crypt, solution):
    d = {}
    for k,v in solution:
        d[k] = v
        
    words = [''.join(["" + d[i] for i in crypt[j]]) for j in range(3)]
    starts_with_zero = any(i.startswith('0') for i in words if len(i) > 1)
    
    return not starts_with_zero and int(words[0]) + int(words[1]) == int(words[2])