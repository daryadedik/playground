# Prettyprint

def pretty_print(A):
    size = 2 * A - 1
    array = [[0 for x in xrange(size)] for y in xrange(size)]

    for i in xrange(0, size):
        for j in xrange(i, size-i):
            array[i][j] = A - i
            array[j][i] = A - i
            array[size-1-i][j] = A - i
            array[j][size-1-i] = A - i

    for i in xrange(0, size):
        print array[i]

pretty_print(4)

#[4, 4, 4, 4, 4, 4, 4]
#[4, 3, 3, 3, 3, 3, 4]
#[4, 3, 2, 2, 2, 3, 4]
#[4, 3, 2, 1, 2, 3, 4]
#[4, 3, 2, 2, 2, 3, 4]
#[4, 3, 3, 3, 3, 3, 4]
#[4, 4, 4, 4, 4, 4, 4]