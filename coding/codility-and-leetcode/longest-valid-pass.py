# Find longest valid password
def is_valid(string):
    num_digits = 0
    num_letters = 0
    for c in string:
        if c.isdigit():
            num_digits += 1
        if c.isalpha():
            num_letters += 1

    return (string.isalnum() and num_letters % 2 == 0 and num_digits % 2 != 0)

def solution(S):
    max_len = -1
    S_arr = S.split()
    for v in S_arr:
        if is_valid(v):
            max_len = max(max_len, len(v))

    return max_len

print(solution("test 5 a0A pass007 ?xy1"))

string = 'slkjmkk,kjjhjhjs,ewewe'
print([x.strip() for x in string.split(',')])