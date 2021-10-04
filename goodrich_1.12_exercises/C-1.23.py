a = [1, 3, 5, 6]

try:
    a[10] = 50
except:
    print("Don’t try buffer overflow attacks in Python!")