def count_vowels(string):
    return sum([i.lower() in ['a', 'o', 'u', 'e', 'i', 'y'] for i in string])


print(count_vowels("Hello worlds!"))