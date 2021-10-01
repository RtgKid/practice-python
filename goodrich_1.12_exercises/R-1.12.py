import random as r

seq = [1, 0, 42, 53, 14, 5]
print(r.choice(seq))


def new_random_choice(data):
    return data[r.randrange(0, len(data))]


print(new_random_choice(seq))