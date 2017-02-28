# Hamming distance. Leetcode
def hammingDistance(x, y):
        count = 0
        binx = "{:064b}".format(x)
        biny = "{:064b}".format(y)
        for i in range(len(binx)):
                if binx[i] != biny[i]:
                        count += 1
        return count

print(hammingDistance(1, 4))