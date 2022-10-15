def minimumSwaps(arr):
    i = 0
    swaps = 0
    while i < len(arr):
        while arr[i] != i + 1:
            a = arr[i]
            arr[i], arr[a - 1] = arr[a - 1], arr[i]
            swaps += 1
        i += 1           
    return swaps    