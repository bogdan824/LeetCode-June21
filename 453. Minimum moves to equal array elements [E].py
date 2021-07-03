'''
Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.

In one move, you can increment n - 1 elements of the array by 1.
'''

def minMov(nums):
	count = 0
	mini = min(nums)
	for i in range(len(nums)):
		diff = nums[i] - mini
		count+=diff 

	return count

#nums = [-1,2,3,5]
#nums = [1,1,1]
nums = [-1,1,2,3]
print(minMov(nums))