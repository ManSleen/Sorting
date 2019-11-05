def selection_sort(arr):

    for position in range(len(arr) - 1):
        smallest_index = position

        for j in range(position + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        print(arr)
        arr[position], arr[smallest_index] = arr[smallest_index], arr[position]
        print(f"Swapped {arr[position]} with {arr[smallest_index]}")

    return arr


my_array = [5, 3, 9, 2, 1, 6]

print(selection_sort(my_array))

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    for k in range(len(arr)):
        for position in range(len(arr) - k - 1):
            if arr[position] > arr[position + 1]:
                arr[position], arr[position + 1] = arr[position + 1], arr[position]
    return arr


my_new_array = [8, 1, 6, 2, 7, 3]

print(bubble_sort(my_new_array))


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
