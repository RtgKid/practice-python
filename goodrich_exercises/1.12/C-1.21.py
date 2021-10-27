def foo():
    l = []
    while True:
        try:
            new_input = input()
            l.append(new_input)
        except:
            for i in range(1, len(l)+1):
                print(l[-i])
            exit(0)


foo()