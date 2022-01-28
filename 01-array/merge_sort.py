def divide(arr: list[int]):
    if len(arr) <= 1:
        return
    
    mid = len(arr)//2
    right = arr[:mid]
    left = arr[mid:]

    divide(left)
    divide(right)

    mergeSort(left, right, arr)


def mergeSort(a: list[int], b: list[int], arr: list[int]):
    lenA = len(a)
    lenB = len(b)
    i = j = k = 0

    while i < lenA and j < lenB:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1
        k+=1

    while i < lenA:
        arr[k] = a[i]
        k += 1
        i += 1
    while j < lenB:
        arr[k] = b[j]
        k += 1
        j += 1
    
    return


if __name__ == '__main__':
    arr = [10, 3, 15, 7, 8, 23, 98, 29]
    divide(arr)
    print(arr)