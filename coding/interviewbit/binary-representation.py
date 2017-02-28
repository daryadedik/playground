# Binary Representation

class Solution:
    # @param A : integer
    # @return a strings
    def findDigitsInBinary(self, A):
        bin = []
        if A == 0:
            return 0
        while A != 1:
            if A % 2 == 0:
                bin.append(str(0))
            else:
                bin.append(str(1))
            A = A / 2

        bin.append(str(1))
        return ''.join(bin[::-1])