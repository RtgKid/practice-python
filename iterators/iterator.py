data = [1,2,3,4]

i = iter(data)
print(i)

print(next(i))

#This does not return list of (0, 9) but returns iterable object
#Lazy evaluation :)
print(range(10))

#This instead makes a list
print(list(range(10)))