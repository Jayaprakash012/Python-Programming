arr = [1, 1, 2, 2, 3, 4, 4]

if len(arr) == 0:
    print([])
else:
    i = 0

    for j in range(1, len(arr)):
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]

    print(arr[:i + 1])