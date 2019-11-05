# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):

    for position in range(len(arr)):
        smallest_index = position

        for j in range(position + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        arr[position], arr[smallest_index] = arr[smallest_index], arr[position]

    return arr


my_array = [5, 3, 9, 2, 1, 6]

print(selection_sort(my_array))

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
