"""
Given an array of integers nums sorted in ascending order, find the starting and 
ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.
"""

def first_and_last(nums, target):
	answer = [-1, -1]
	i = 0
	j = len(nums)-1
	if  len(nums) < 1:
		return answer
	while nums[i] != target and i<len(nums)-1:
		i+=1

	while nums[j] != target and j>0:
		j-=1
	
	if nums[i] == nums[j] == target:
		return [i,j]
	return answer

#nums = [5,7,7,8,8,10] #target = 8
#nums = [5,7,7,8,8,10] #target = 6
nums = [1] #target = 0
target = 0

print(first_and_last(nums,target))
