try:
    age = int(input("Enter some number"))
except EOFError:
    print("Something wrong happened")
except ValueError:
    print("That is invalid age")