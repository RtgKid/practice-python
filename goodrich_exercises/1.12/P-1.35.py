import random


def generate_random_birthday():
    return random.randint(0, 365)


def generate_random_class(n):
    birthdays = []
    for i in range(n):
        birthdays.append(generate_random_birthday())
    return birthdays


def is_birthday_repeats_in_class(days):
    return sum([i == j for i in days for j in days]) > len(days)


def simulate(n, times):
    for _ in range(times):
        print(is_birthday_repeats_in_class(generate_random_class(n)))


simulate(n=25, times=10)


