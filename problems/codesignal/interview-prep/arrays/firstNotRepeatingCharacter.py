def solution(s):
    d = {}
    unique = []
    
    for i in s:
        if d.get(i, 0) == 0:
            unique.append(i)
        elif d.get(i) == 1:
            unique.remove(i)
        
        d[i] = d.get(i, 0) + 1    
    
    if len(unique) == 0:
        return "_"
    else:
        return unique[0]    
                