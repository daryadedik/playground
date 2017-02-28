# 54. Spiral Matrix. Leetcode and Spiral Order Matrix I on interviewbit
def spiralOrder(A):
        res = []
        if not A:
            return []
        i, j, di, dj = 0, 0, 0, 1
        m, n = len(A), len(A[0])
        for v in xrange(m * n):
            res.append(A[i][j])
            A[i][j] = ''
            if A[(i+di)%m][(j+dj)%n] == '':
                di, dj = dj, -di
            i += di
            j += dj
        return res

print(spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))