def one_away(s1: str, s2:str) -> bool:
    diff_count = 0
    i = 0
    if (len(s1) - len(s2)) == 0:
        if sum([int(s1[i] != s2[i]) for i in range(len(s1))]) > 1:
            return False
        else:
            return True
    elif abs(len(s1) - len(s2)) > 1:
        return False
    else:
        l = max(len(s1), len(s2))            
        j = i
        while i < l-1:
            if s1[i] != s2[j]:
                diff_count += 1
                i+=1
            else:
                i+=1
                j+=1
        return diff_count <= 1            

print(one_away("pale", "palie"))
print(one_away("pales", "pale"))
print(one_away("pale", "bale"))
print(one_away("pale", "balo"))
print(one_away("pale", "bae"))