# Count Element Occurence

def findCount(A, B):
    begin, end = 0, len(A) - 1
    firstOcc = -1

    while begin <= end:
        mid = (begin + end) / 2
        if A[mid] == B:
            firstOcc = mid
            end = mid - 1
        elif B > A[mid]:
            begin = mid + 1
        else:
            end = mid - 1

    if firstOcc == -1:
        return 0

    begin, end = firstOcc, len(A) - 1
    secondOcc = -1

    while begin <= end:
        mid = (begin + end) / 2
        if A[mid] == B:
            secondOcc = mid
            begin = mid + 1
        elif B > A[mid]:
            begin = mid + 1
        else:
            end = mid - 1

    return secondOcc - firstOcc + 1

print(findCount([5, 7, 8, 8, 8, 8, 10], 8))