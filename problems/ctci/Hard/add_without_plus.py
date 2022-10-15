def add(a : int, b : int) -> int :
    while b != 0:
        c = a ^ b
        b = (a & b) << 1
        a = c
    return a 


print(add(5, 6))    

