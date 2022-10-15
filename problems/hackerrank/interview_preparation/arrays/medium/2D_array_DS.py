def hourglassSum(arr):
    n = len(arr)
    m = -100
    for j in range(n-2):
        for i in range(n-2):
            s = arr[i][j] + arr[i][j+1] + arr[i][j+2]
            s += arr[i+1][j+1]
            s += arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            print(s)   
            if s > m:
                m = s
            
    return m