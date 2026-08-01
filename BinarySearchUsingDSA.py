arr = [1, 2, 3, 4, 5]
key = int(input("Enter the key to search: "))
low = 0
high = len(arr) -1
 
while low <= high:
    mid = (low + high) // 2
    if arr[mid] == key:
        print("key found at the index:",mid)
        break
    elif arr[mid] < key:
        low = mid + 1
    else:
        high = mid - 1 
else:
    print("key not found")           
         