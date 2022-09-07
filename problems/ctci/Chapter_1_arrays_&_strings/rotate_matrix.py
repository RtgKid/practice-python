def rotate_matrix(m):
    n = len(m)
    i = j = 0

    while i < n:
        while j < n:
            m[j][i], m[i][j] = m[i][j], m[j][i]
            j+=1
        i += 1
        j = i    

    for i in range(n):
        m[i][n-1], m[i][0] = m[i][0], m[i][n-1]
    return m

print(rotate_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

# 1 2 3  1 4 7
# 4 5 6  2 5 8
# 7 8 9  3 6 9

# 7 4 1
# 8 5 2
# 9 6 3
