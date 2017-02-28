import urlparse
string = "10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] GET http://www.the-associates.co.uk/assets/js/the-associates.js HTTP/1.1 200 10469"
substr = "http://www.the-associates.co.uk"
lens = len(substr)
arr = string.strip().split(' ')
url = urlparse.urlparse(arr[6]).path
print(url)

print(arr)
#mapper
"""
import sys

for line in sys.stdin:
    data = line.strip().split(' ')
    if len(data) == 10:
        ip, identity, username, date, zone, method, page, query, status, size = data
        print "{0}\t{1}".format(page, 1)

"""