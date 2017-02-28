# Check if password is valid
def is_valid(substr):
    """
    Checks if substr is a valid password
    """
    return (any(x.isupper() for x in substr)
            and all(not x.isdigit() for x in substr))

def solution(S):
    """
    Finds the longest valid password substring in S
    """
    max_len = -1 # length of the longest substring
    for i in xrange(len(S)):
        for j in xrange(i + 1, len(S) + 1):
            if is_valid(S[i:j]):
                max_len = max(max_len, j - i)
    return max_len

print(solution('a0cbbQ'))