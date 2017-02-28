# 476. Number Complement. Leetcode
def findComplement(num):
        bin_n = "{0:b}".format(num)
        flipped = [str(int(val) ^ 1) for val in bin_n]
        return int(''.join(flipped), 2)

print findComplement(5)