my_string = "Hello world"
print(my_string[-1])

# my_string[3] = 'X' string does not support item assignment

print(my_string[::-1])

if "X" in my_string:
    print("X" + " is in " + my_string)

my_string = '      Hello String   '
my_string = my_string.strip();
print(my_string)   

print(my_string.startswith("Hello"))
print(my_string.endswith("Hello"))
print(my_string.find("lo"))
print(my_string.count("l"))


#lets split the list
my_string = "How are you doing"
my_list = my_string.split()
print(my_list)

#lets collect it back
new_string = " ".join(my_list)
print(new_string)

#f-strings
var = "Tom"
my_string = "the var is %s" % var
print(my_string)
my_string = "the var is {}".format(var)
print(my_string)
print(f"the var is {var}")