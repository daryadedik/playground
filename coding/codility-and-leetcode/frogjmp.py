import math
# Codility. FrogJmp
def frogjmp(X, Y, D):
    if X < 1 or Y < 1 or D < 1 or X > Y:
        return 0

    if (Y - X) % D:
        return (Y - X) / D + 1
    return (Y - X) / D

    #return int(math.ceil(float((Y - X)) / D))

print(frogjmp(10, 85, 30))
print(frogjmp(8, 2, 40))
print(frogjmp(0, 0, 0))
print(frogjmp(10, 0, 0))
print(frogjmp(10, 120, 30))
print(frogjmp(10, 1000000000, 100))