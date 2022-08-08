from tokenize import maybe


a = (16, 13, 5)

print(a)

print(a[0])

#a[0] = 5 #Tupples are immutable

b = (18) #This is just an integer
print(b)


c = (18,) #This is a tuple with 1 element
print(c)

b = "banana", "apple"
print(b)
print(type(b))

c = ["banana", "apple"]
tup = tuple(c)
print(tup)

if "banana" in tup:
    print("yes")

print(len(tup))    
print(tup.count("banana"))
print(tup.index("banana"))

print(list(tup))


my_tuple = (0, 1, 3, 4, 5, 6)
i1, *i2, i3 = my_tuple

print(i1, i2, i3)