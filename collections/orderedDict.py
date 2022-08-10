from collections import OrderedDict

ordered_dict = OrderedDict()
ordered_dict['a'] = 2
ordered_dict['b'] = 3
ordered_dict['c'] = 4
ordered_dict['d'] = 5

print(ordered_dict)


#starting from 3.6 normal dict also keeps the order
normal_dict = {}
normal_dict['a'] = 2
normal_dict['b'] = 3
normal_dict['c'] = 4
normal_dict['d'] = 5
print(normal_dict)