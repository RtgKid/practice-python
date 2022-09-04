def URLify(s:str) -> str:
   return s.replace(" ", "%20")


print(URLify("Okay lets test this!"))


def URLify_in_place(a: str, l: int) -> str:
    s = list(a)
    i = len(s)-1
    l = l - 1
    while i != 0:
        if s[l] != ' ':
            s[i] = s[l] 
            i = i - 1
        else:
            s[i] = '0'
            s[i-1] = '2'
            s[i-2] = '%'
            i = i - 3
        l = l - 1
    return ''.join(s)

print(URLify_in_place("Mr 3ohn Smith    ", 13))
print(URLify_in_place("Okay lets  ", 8))
print(URLify_in_place("Okay lets test this!      ", 20))