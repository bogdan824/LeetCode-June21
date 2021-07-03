"""
You are given an integer n. An array nums of length n + 1 is generated in the following way:
nums[0] = 0
nums[1] = 1
nums[2 * i] = nums[i] when 2 <= 2 * i <= n
nums[2 * i + 1] = nums[i] + nums[i + 1] when 2 <= 2 * i + 1 <= n
Return the maximum integer in the array nums​​​.
"""

def maximumGenerated(n):
	if n == 0:
		return 0 
	keep = [0, 1]

	for i in range (2,n+1):
		if i%2==0:
			keep.append(keep[i//2])
		else:
			keep.append((keep[i//2]) + (keep[i//2 + 1]))
	return max(keep)




n = 7
print(maximumGenerated(n))