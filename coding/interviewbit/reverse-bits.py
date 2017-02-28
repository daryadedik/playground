# Reverse Bits

def reverse(A):
        return int('{:032b}'.format(A)[::-1], 2) #8bits will be {:08b}
print(reverse(3))