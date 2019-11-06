# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Loop through merged_arr that we just created. for each element...
    for index in range(len(merged_arr)):
        # make sure both arrays aren't empty
        if len(arrA) > 0 and len(arrB) > 0:
            # check first element of each array, see which is smaller
            # If arrA[0] is smaller, add it to merged_arr and delete it from arrA
            if arrA[0] < arrB[0]:
                merged_arr[index] = arrA[0]
                arrA.remove(arrA[0])
            # If arrB[0] is smaller, add it to merged_arr and delete it from arrB
            else:
                merged_arr[index] = arrB[0]
                arrB.remove(arrB[0])
        # if either array is empty:
        else:
            if len(arrA) == 0:
                # is arrA is empty, add the next element from arrB to merged_arr and delete it from arrB
                merged_arr[index] = arrB[0]
                arrB.remove(arrB[0])
            else:
                #  otherwise if arrB is empty, add the next element from arrA and then delete it from arrA
                merged_arr[index] = arrA[0]
                arrA.remove(arrA[0])
    print("Merging:", merged_arr)
    return merged_arr


# print(merge([9, 23], [
#       20]))

# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    print("Splitting:", arr)
    if len(arr) <= 1:
        return arr

    m = len(arr)//2
    l = merge_sort(arr[:m])
    r = merge_sort(arr[m:])

    return merge(l, r)


print(merge_sort([25, 1, 7, 3, 5, 8, 20, 23, 9]))

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
