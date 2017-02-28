# Roman To Integer

def roman_to_integer(A):
    L = [i for i in A]
    L.append('P')
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'P': 0}
    integer = 0
    for i in xrange(len(L)-1):
        if romans[L[i]] >= romans[L[i+1]]:
            integer += romans[L[i]]
        else:
            integer -= romans[L[i]]

    return integer

print(roman_to_integer("MMMCCLXXXVII"))
print(roman_to_integer("MDCCCIV")) #1000+500+100+100+100-1+5 = 1804
print(roman_to_integer("MMCDLXXV")) #1000+1000-100+500+50+10+10+5 = 2475