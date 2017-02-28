# Compute hamming weight

def hammingWeight(n):
    binr= "{0:b}".format(n)
    sum=0
    for i in binr:
        sum += int(i)
    print(sum)

hammingWeight(5)

#461. Hamming Distance. Leetcode
def hammingDistance(x, y):
        count = 0
        binx = "{:064b}".format(x)
        biny = "{:064b}".format(y)
        for i in range(len(binx)):
                if binx[i] != biny[i]:
                        count += 1
        return count