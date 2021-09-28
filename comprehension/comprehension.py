# Traditional
squares = []
for i in range(1, 5):
    squares.append(i*i)
print(squares)


print([i*i for i in range(1, 5)])
# Factors of 10
print([k for k in range(1, 10 + 1) if 10 % k == 0])

# Syntax
# [ k for k in range(0,n)] list
# ( k for k in range(0,n)) generator
# { k for k in range(0,n)} set
# { k : k for k in range(0,n)} dictionary

# This is cool, as we want to compute but not store the results in memory
print(sum(k for k in range(1, 10)))

