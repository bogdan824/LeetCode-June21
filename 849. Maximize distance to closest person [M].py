"""
You are given an array representing a row of seats where seats[i] = 1 represents a person 
sitting in the ith seat, and seats[i] = 0 represents that the ith seat is empty (0-indexed).
There is at least one empty seat, and at least one person sitting.
Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 
Return that maximum distance to the closest person.
"""

def maximize_distace(seats):
	l = -1
	n = len(seats)
	maxDist = 0
	for i in range(len(seats)):
		if seats[i] == 1:
			if l == -1:
				maxDist = i
			else:
				maxDist = max(maxDist, (i-l)//2)
			l = i
	if seats[n-1] == 0:
		maxDist = max(maxDist,n-1-l)
	return maxDist



#seats = [1,0,0,0,1,0,1]
seats = [1,0,0,0]
print(maximize_distace(seats))