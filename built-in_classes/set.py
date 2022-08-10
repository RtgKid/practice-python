a = {"a", "b", "c"}
print(a)

b = {} #This won't create an empty set, instead it creates an empty dict
print(type(b))

c = set()
print(c)

myset = set("Hello")
print(myset)

myset = set([1, 2, 3, 1, 2])
print(myset)

myset.add(5)
print(myset)

#Remove without key error
myset.discard(6)
print(myset)

#Union
odds = {1, 3, 5, 7, 9}
evens = {2, 4, 6, 8, 10}
primes = {2, 3, 5, 7}

u = odds.union(evens)
print(u)

i = odds.intersection(evens)
print(i)

i = odds.intersection(primes)
print(i)

d = primes.difference(evens)
print(d)

sd = primes.symmetric_difference(evens)
print(sd)

#subset and superset
print(evens.issubset(odds))
print(evens.issuperset(odds))
print(evens.isdisjoint(odds))