def solution(a):
    occ_ind = -1
    d = {}
    for idx, i in enumerate(a):
        if i not in d:
            d[i] = 0
        else:
            occ_ind = idx
            return a[occ_ind]        
    return -1
