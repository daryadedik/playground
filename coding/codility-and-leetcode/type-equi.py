# Codility. TapeEquilibrium
def type_equilibrium(a):
    if len(a) == 0:
        return 0

    diffs = []
    l = a[0]
    r = sum(a[1:len(a)])
    diffs.append(abs(l - r))

    for i in range(1, len(a) - 1):
        l += a[i]
        r -= a[i]
        diffs.append(abs(l - r))

    return min(diffs)

print(type_equilibrium([3, 1, 2, 4, 3]))
print(type_equilibrium([3, 6, 7, 1, 2, 9, 3, 5]))
print(type_equilibrium([]))
print(type_equilibrium([0, 1, 0]))
print(type_equilibrium([1, 2]))
print(type_equilibrium([0]))
print(type_equilibrium([1]))
print(type_equilibrium([-2, -15, 4, -12, 20]))