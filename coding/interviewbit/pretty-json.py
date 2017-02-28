# Pretty Json

class Solution:
    def __init__(self):
        self.l = []

    # @param A : string
    # @return a list of strings
    def prettyJSON(self, A):
        self.l = []
        if A:
            self._pretty(A)
        return self.l

    def _pretty(self, A, b=0, indent=''):
        i = b
        while i < len(A):
            if A[i] == '{' or A[i] == '[':
                if b < i and A[b:i].strip():
                    self.l.append(indent + A[b:i].strip())
                self.l.append(indent + A[i])
                i = self._pretty(A, i+1, indent + '\t')
                if i < len(A):
                    if i + 1 < len(A) and A[i+1] == ',':
                        self.l.append(indent + A[i:i+2])
                        i += 1
                    else:
                        self.l.append(indent + A[i])
                i += 1
                b = i
            elif A[i] == '}' or A[i] == ']':
                if b < i and A[b:i].strip():
                    self.l.append(indent + A[b:i].strip())
                return i
            elif A[i] == ',':
                self.l.append(indent + A[b:i+1].strip())
                i += 1
                b = i
            else:
                i += 1
        return i