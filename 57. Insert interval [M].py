"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
You may assume that the intervals were initially sorted according to their start times.
"""

def insert_interval(intervals,newInterval):
	intervals.append(newInterval)
	intervals.sort()
	keep = [] 

	start = intervals[0][0]
	end = intervals[0][1]

	for i in intervals:
		if i[0] > end:
			keep.append([start,end])
			start,end = i[0],i[1]
		else:
			end = max(end,i[1])
	keep.append([start,end])
	return keep





intervals = [[1,3],[6,9]]
newInterval = [2,5]
print(insert_interval(intervals,newInterval))