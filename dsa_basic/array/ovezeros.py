
def pushZerosToEnd( arr : list) -> list:
    count = 0

    for i in range(len(arr)):
        print(f'current count: {count} and for idx: {i} and arr: {arr}')
        if arr[i] != 0:

            arr[i], arr[count] = arr[count], arr[i]
            count += 1

    return arr


arr = [1, 2, 0, 4, 3, 0, 5, 0]

print(pushZerosToEnd(arr))







