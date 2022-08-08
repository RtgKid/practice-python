from re import M


mylist = ["banana", "apple", "cherry"]
print(mylist)

if "banana" in mylist:
    print("Banana is in the list")

#Add 
mylist.append("lemon")
print(mylist)

# Add at specific index
mylist.insert(1, "blueberry")
print(mylist)

#Remove items
removed_item = mylist.pop()
print(removed_item)
print(mylist)

#Remove specific element
cherry = mylist.remove("cherry") #this does not return anything
print(cherry) 
print(mylist)

#Clear mylist.clear()

#Reverse
mylist.reverse()
print(mylist)

#Sort
mylist.sort()
print(mylist)

#Create new list with the same element
mylist1 = [0] * 5
print(mylist1)

#Concat
mylist2 = [1] * 6
mylist = mylist1 + mylist2
print(mylist)

#Slicing
mylist = [1, 2, 3, 4, 5, 6]
a = mylist[2:3]
print(a)

b = mylist[3:]
print(b)

c = mylist[:6]
print(c)

d = mylist[3:6:2]
print(d)

e = mylist[::-1]
print(e)

#Copy
list_org = ["banana", "apple", "cherry"]
list_cpy = list_org
print(list_org)
print(list_cpy)

list_cpy.append("lemon")
print(list_org)
print(list_cpy)

list_copy_actual = list_org[:] # This makes a copy
list_copy_actual.append("peach")
print(list_org)
print(list_copy_actual)