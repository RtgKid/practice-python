from collections import Counter

a = "aaaaabbbbcccdd"
my_counter = Counter(a)
print(my_counter)
print(my_counter.items())

print(my_counter.most_common(1)) 
print(my_counter.most_common(1)[0])
print("Most common element in the string", my_counter.most_common(1)[0][0])

print(list(my_counter.elements()))