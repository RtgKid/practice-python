from collections import OrderedDict

def solution(s):
    d = OrderedDict()

    for i in s:
        if i not in d:
            d[i] = 1
        else:
            d[i] = d[i] + 1    
                
    for k, v in d.items():
        if v == 1:
            return k
    else:
        return "_"                 
            