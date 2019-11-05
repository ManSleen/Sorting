# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    j = 0
    k = 0
    for index in range(len(merged_arr)):
        if j < len(arrA) and arrA[j] < arrB[k]:
            print("arrA[j]", arrA[j])
            merged_arr[index] = arrA[j]
            j += 1
        elif (k < len(arrB)):
            print("arrB[k]", arrB[k])
            merged_arr[index] = arrB[k]
            k += 1

    return merged_arr


print(merge([1, 2, 4, 7, 9], [3, 5, 6, 8, 10]))

# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    # TO-DO

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
