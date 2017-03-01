# Udacity "Intro to Hadoop and MapReduce"
# Total Sales

# mapper
import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        date, time, store, item, cost, payment = data
        print "{0}\t{1}".format(store, cost)

# reducer
import sys

totalSales = 0
numSales = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thisKey, thisSale = data_mapped
    totalSales += float(thisSale)
    numSales += 1

print totalSales, "\t", numSales