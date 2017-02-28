string = "10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] GET /assets/js/the-associates.js HTTP/1.1 200 10469"

arr = string.strip().split(' ')
print(arr[6])
print(arr[6] == "/assets/js/the-associates.js")

#mapper
"""
import sys

for line in sys.stdin:
    data = line.strip().split(' ')
    if len(data) == 10:
        ip, identity, username, date, zone, method, page, query, status, size = data
        print "{0}\t{1}".format(page, 1)

# reducer
import sys

totalPage = 0
oldPage = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thisPage, thisCount = data_mapped
    if oldPage and oldPage != thisPage:
        print oldPage, "\t", totalPage
        totalPage = 0

    oldPage = thisPage
    totalPage += float(thisCount)
"""



