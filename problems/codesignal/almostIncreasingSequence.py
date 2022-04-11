def solution2(s):
    error_count = 0
    skip_forward = False
    skip_back = False
    for i in range(len(s) - 1):
        if s[i] >= s[i+1]:
            if i < len(s) - 2 and s[i] >= s[i + 2]:
                skip_forward = True
            if i > 0 and s[i-1] >= s[i+1]:
                skip_back = True    
            error_count+= 1
            if (error_count > 1 or (skip_forward == True and skip_back == True)):
                return False
    return True            




print(solution2([10, 1, 2, 3, 4, 5]) == True)
print(solution2([1, 2, 5, 3, 5])==True)

print(solution2([1,2,1,2]) == False)
print(solution2([1, 2, 3, 4, 3, 6]) == True)

print(solution2([3, 5, 67, 98, 3]) == True)

print(solution2([1, 2, 18, 4, 4]) == False)
print(solution2([1, 2, 3, 4, 5, 3, 5, 6]) == False)
