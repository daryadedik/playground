# Udacity "Intro to Hadoop and MapReduce"
# Highest Sale

# mapper
import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        date, time, store, item, cost, payment = data
        print "{0}\t{1}".format(store, cost)

# reducer
import sys

maxSale = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thisKey, thisSale = data_mapped
    if oldKey and oldKey != thisKey:
        print oldKey, "\t", maxSale
        oldKey = thisKey
        maxSale = 0
    else:
        if float(thisSale) > float(maxSale):
            maxSale = thisSale
    oldKey = thisKey

if oldKey != None:
    print oldKey, "\t", maxSale