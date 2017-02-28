# Search For A Range
def searchRange(self, A, B):
        begin, end = 0, len(A)-1
        firstOcc = secondOcc = -1
        interval = [-1, -1]

        while begin <= end:
            mid = (begin + end) / 2
            if A[mid] == B:
                firstOcc = mid
                end = mid - 1
            elif B > A[mid]:
                begin = mid + 1
            else:
                end = mid - 1

        interval[0] = firstOcc

        begin, end = firstOcc, len(A) - 1

        while begin <= end:
            mid = (begin + end) / 2
            if A[mid] == B:
                secondOcc = mid
                begin = mid + 1
            elif B > A[mid]:
                begin = mid + 1
            else:
                end = mid - 1

        interval[1] = secondOcc

        return interval