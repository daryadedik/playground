# Compare Version Numbers

from functools import reduce

def compareVersion(A, B):
    go = lambda x: reduce(lambda x, y: x*10+y, map(int, x.split('.')), 0)
    return go(A) < go(B)

print(compareVersion('13.0', '13.0.8'))
print(compareVersion('002', '10'))
print(compareVersion('1002', '10'))
