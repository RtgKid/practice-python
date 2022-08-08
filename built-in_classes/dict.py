empty_dict = {}
print(empty_dict)

d = {"1": "one", "2": "two"}
print(d)
d["1"] = "uno"
print(d)

#Delete 
del d["1"]
print(d)

two = d.pop("2")
print(two)
print(d)

#Check if has
if "1" not in d:
    d["1"] = "one"
print(d)



pair = [('ga', 'Irish'), ('de', 'German')]
new_dict = dict(pair)
print(new_dict)
print(new_dict['ga'])

#Looping
for key, value in new_dict.items():
    print(key, value)

#Copy
new_dict_cpy = dict(new_dict)
new_dict_cpy["am"] = "Armenian"
print(new_dict_cpy)

#Update/concat
new_dict.update(new_dict_cpy)
print(new_dict)

