# Invert string
def invert(S):
  S_c = ''.join(S[-i] for i in range(1, len(S) + 1))
  S_c = S[::-1]
  return S_c


print(invert('asdf'))
print(invert(''))
print(invert('abcde'))
print(invert('ab'))