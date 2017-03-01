# Udacity "Intro to Hadoop and MapReduce"
# Most Popular

# mapper
import sys
import urlparse

for line in sys.stdin:
    data = line.strip().split(" ")
    if len(data) == 10:
        url = urlparse.urlparse(data[6]).path
        print "{0}\t{1}".format(url, "pathhit")

# reducer

# reducer
import sys

index = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thisKey, pathHit = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", index
        oldKey = thisKey
        index = 0

    oldKey = thisKey
    index += 1

if oldKey != None:
    print oldKey, "\t", index