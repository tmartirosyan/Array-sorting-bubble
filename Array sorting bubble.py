# first algorithm //bubble
def bubbleSortArray(array):
    index = 0
    iteration_count = 0
    while index < len(array) - 1:
        if array[index] > array[index + 1]:
            num = array[index + 1]  # vercrec 2
            array[index + 1] = array[index]  # 2 -> 8
            array[index] = num  # 8 -> 2
            iteration_count += 1
        index += 1
    if iteration_count >= 1:
        return bubbleSortArray(array)
    else:
        return array


array = [0, 4, 2, 7, 6, 3, 5, 1]
print(bubbleSortArray(array))
