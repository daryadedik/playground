# Codility. GenomicRangeQuery
def genomic_range(S, P, Q):
    ratemap = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    min_rate = [0] * len(Q)
    dist = [[len(S)] * len(S) for i in range(len(ratemap))]

    for i, c in enumerate(S):
        for row in dist:
            row[i] = row[i-1] + 1
        dist[ratemap[c]-1][i] = 0
    for j, i in enumerate(Q):
        for k, row in enumerate(dist):
            if row[i] <= i - P[j]:
                min_rate[j] = k + 1
                break
    return min_rate


def genomic_range1(S, P, Q):
    ratemap = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    min_rate = [0] * len(P)

    for i in range(len(P)):
        min_rate[i] = min(ratemap[c] for c in S[P[i]:Q[i]+1])
        #print(S[P[i]:Q[i]+1])
    return min_rate


print(genomic_range('AGCCTA', [2, 5, 1], [4, 5, 3]))
print(genomic_range1('AGCCTA', [2, 5, 1], [4, 5, 3]))
print(genomic_range('CATAGCCTTGT', [0, 4, 7, 7, 0], [3, 7, 8, 10, 10]))
print(genomic_range1('CATAGCCTTGT', [0, 4, 7, 7, 0], [3, 7, 8, 10, 10]))