def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array
array = [34,4,464,532,1,9,46,89,567,7,12,67,87]
print(f'Unsorted list {array}')
print("-------------------------")
bubble_sort(array)
print(f'Sorted list is: {array}')

def binary_search(element, array):
    first = 0
    last = len(array) - 1
    ResultOk = False
    Pos = -1
    while first <= last:
        middle = (first+last) // 2
        if element == array[middle]:
            ResultOk = True
            Pos = middle
            break
        elif element > array[middle]:
            first = middle + 1
        else:
            last = middle - 1
    return ResultOk, Pos
Array = array
element = 67
ResultOk, Pos = binary_search(element, array)
print("-------------------------")
if ResultOk:
    print(f'Item found!: Place {Pos}')
else:
    print('Item not found! ')














