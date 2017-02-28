# Compare Version Numbers

def compareVersion(A, B):
    v1Arr = A.split('.')
    v2Arr = B.split('.')
    len1 = len(v1Arr)
    len2 = len(v2Arr)
    lenMax = max(len1, len2)
    for x in range(lenMax):
        v1Token = 0
        if x < len1:
            v1Token = int(v1Arr[x])
        v2Token = 0
        if x < len2:
            v2Token = int(v2Arr[x])
        if v1Token < v2Token:
            return -1
        if v1Token > v2Token:
            return 1
    return 0

print(compareVersion('13.0', '13.0.8'))
print(compareVersion('002', '10'))