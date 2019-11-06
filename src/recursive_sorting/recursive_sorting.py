# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # k, j = 0, 0
    for index in range(len(merged_arr)):
        if len(arrA) > 0 and len(arrB) > 0:
            if arrA[0] < arrB[0]:
                print("arrA[0]:", arrA[0])
                merged_arr[index] = arrA[0]
                arrA.remove(arrA[0])
            else:
                print("arrB[0]:", arrB[0])
                merged_arr[index] = arrB[0]
                arrB.remove(arrB[0])
        else:
            if len(arrA) == 0:
                merged_arr[index] = arrB[0]
                arrB.remove(arrB[0])
            else:
                merged_arr[index] = arrA[0]
                arrA.remove(arrA[0])

    return merged_arr


print(merge([1, 3, 5, 7, 8, 9, 20, 23, 25, 27], [
      2, 4, 6, 10, 11, 12, 17, 18, 19, 21, 50, 55, 100, 140]))

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
