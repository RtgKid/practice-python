def zero_matrix(M, m, n):
    i = j = 0
    zero_r = set()
    zero_c = set()
    while i < m:
        while j < n:
            if M[i][j] == 0:
                zero_r.add(i)
                zero_c.add(j)
            j+=1
        j=0    
        i+=1        
    
    for i in zero_r:
        M[i] = [0] * n

    for i in zero_c:
        for j in range(m):
            M[j][i] = 0
    print(M)


zero_matrix([[1, 2, 3, 0], [4, 5, 6, 9]], 2, 4)    

zero_matrix([[1, 2, 3, 0], [4, 5, 6, 9], [4, 6, 2, 5], [0, 4, 5, 1]], 4, 4)    