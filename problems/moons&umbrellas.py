# Link to the problem 
# https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d1145

# 4
# 2 3 CJ?CC?
# 4 2 CJCJ
# 1 3 C?J
# 2 5 ??J???


def calc_cost(x, y, S):
    l = fix_string(S)
    cost = 0
    prev = None
    for i in range(len(l)-1):
        s = l[i]+l[i+1]
        if s == 'CJ':
            cost += x
            prev = l[i]
            continue
        if s == 'JC':
            cost+=y
            prev = l[i]
            continue
    return cost


def fix_string(S):
    l = [str(i) for i in S]
    l, i = c(l)

    while i < len(l) - 1:
        if l[i] == '?':
            if l[i+1] != '?' and l[i-1] != '?':
                if l[i+1] == l[i-1]:
                    l[i] = l[i+1]
                else:
                    l[i] = 'C'    
            else:
                l[i] = l[i - 1]            
        i = i + 1

    if l[i] == '?':
        l[i] = l[i - 1]    

    return l    
      

def c(S):
    l = [str(i) for i in S]
    i = 0
    if l[i] == '?':
        while (l[i] == '?'):
            i = i + 1    
        l[0:i] = l[i] * i    
    return l, i

def main ():
    n = int(input())
    for i in range(n):
        line = input()
        x, y, S = line.split()
        print("Case #" + str(i) + ": " + str(calc_cost(int(x), int(y), S)))


main()    


print(calc_cost(4, 2, "CJCJ") == 10)
print(calc_cost(1, 3, "C?J") == 1)
print(calc_cost(2, 3 , "CJ?CC?") == 5)
print(calc_cost(2, 5, "??J???") == 0)