# Codility. CountDiv
def count_div(A, B, K):
    if A % K:
        A += K - A % K
    return (B - B % K - A) / K + 1

print(count_div(4, 11, 3))
print(count_div(2, 20, 2))
print(count_div(1, 10, 1))
print(count_div(2, 12, 2))
print(count_div(4, 6, 5))
print(count_div(4, 5, 4))
print(count_div(1, 4, 7))
print(count_div(5, 5, 5))
print(count_div(5, 5, 1))