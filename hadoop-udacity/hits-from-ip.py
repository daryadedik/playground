# Udacity "Intro to Hadoop and MapReduce"
# Hits from IP

#mapper
import sys

for line in sys.stdin:
    data = line.strip().split(' ')
    if len(data) == 10:
        ip, identity, username, date, zone, method, page, query, status, size = data
        print "{0}\t{1}".format(ip, 1)

# reducer
import sys

totalPage = 0
neededPage = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thisPage, thisCount = data_mapped
    if thisPage == "10.99.99.186":
        totalPage += float(thisCount)
        neededPage = thisPage

if neededPage != None:
    print neededPage, "\t", totalPage