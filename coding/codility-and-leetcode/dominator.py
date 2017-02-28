# Find dominator: element that appears more than a hafl times in array
def dominator(A):

    element = ''
    count = 0

    for elem in A:
        if element == '':
            element = elem
            count += 1
        else:
            if elem != element:
                element = ''
                count -= 1
            else:
                count += 1

    cnt = 0
    l_ind = -1

    for ind, val in enumerate(A):
        if A[ind] == element:
            cnt += 1
            if l_ind < 0:
                l_ind = ind

    if (cnt >= len(A)//2):
        return l_ind
    else:
        return -1

arr = [1, 2, 4, 3, 4, 2, 2, 4, 4]
ind = dominator(arr)
print(len(arr))
print("Array: {}".format(arr))
print("Index: {}, element: {}".format(ind, arr[ind]))
