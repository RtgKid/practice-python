def minmax(data):
    min_num = 100000
    max_num = -1
    for num in data:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num

    return min_num, max_num


print(minmax([1, 3, 5, 6, 10]))
