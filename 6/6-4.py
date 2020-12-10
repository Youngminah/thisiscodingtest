array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quickSort(array, left, right):

    if left >= right:
        return

    pivot = left
    s = left + 1
    d = right

    while s <= d:
        while s <= right and array[s] <= array[pivot]:
            s += 1
        while d > left and array[d] >= array[pivot]:
            d -= 1
        if s <= d:
            array[s], array[d] = array[d], array[s]

    array[d], array[pivot] = array[pivot], array[d]
    quickSort(array, left, d - 1)
    quickSort(array, d+1, right)


quickSort(array, 0, len(array) - 1)
print(array)
