import random as rand


def my_shuffle(data):
    for _ in range(len(data)):
        first_index = rand.randint(0, len(data) - 1)
        second_index = rand.randint(0, len(data) - 1)
        data[first_index], data[second_index] = data[second_index], data[first_index]


data = [1, 2, 3, 4, 90, 5]
my_shuffle(data)
print(data)
