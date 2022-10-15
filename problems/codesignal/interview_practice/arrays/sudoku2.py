def solution(grid):
    n = len(grid)
    # row case
    for i in grid:
        if not checkline(i):
            return False
               
    # column case
    for i in range(n):
        l = []
        for j in range(n):
            l.append(grid[j][i])
        if not checkline(l):
            return False
    
    # 3x3 cubes 
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not checkline(grid[i][j:j+3] + grid[i+1][j:j+3] + grid[i+2][j:j+3]):
                return False
                       
    return True
    
def checkline(l):
    if '.' in l:
        l = list(filter(lambda a: a != '.', l))
    s = set(l)
    if len(s) != len(l):
        return False
    return True   