# Merge two intervals
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

def merge(self, intervals):
        if not intervals:
            return []
        intervals.sort(key=lambda i: i.start)
        out = []
        cur = intervals[0]
        for i in intervals:
            if i.start <= cur.end:
                cur.end = max(cur.end, i.end)
            else:
                out.append(cur)
                cur = i
        out.append(cur)
        return out

