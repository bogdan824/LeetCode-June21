"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.
"""

def merge_intervals(intervals):
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


intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge_intervals(intervals))