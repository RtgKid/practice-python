def no_punctuation(string):
    new_string = ""
    for i in string:
        if ord(i) in range(97, 97 + 26) or ord(i) in range(56, 56 + 26) or i == ' ':
            new_string += i

    return new_string


print(no_punctuation("Hello world, have fun!"))