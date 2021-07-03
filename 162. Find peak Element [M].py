"""
A peak element is an element that is strictly greater than its neighbors.
Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.
You may imagine that nums[-1] = nums[n] = -∞.
You must write an algorithm that runs in O(log n) time.
"""
def findpeak_element(nums):
	if len(nums)<2:
		return 0
	if len(nums)<3:
		return nums.index(max(nums))
	nums.append(0)
	for i in range(len(nums)):
		if nums[i]>nums[i+1] and nums[i]>nums[i-1]:
			return i

#nums = [1,2,3,1]
nums = [2,3,]
print(findpeak_element(nums))