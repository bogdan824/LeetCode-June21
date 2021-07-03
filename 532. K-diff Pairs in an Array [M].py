"""
Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.
A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:
0 <= i < j < nums.length
|nums[i] - nums[j]| == k
Notice that |val| denotes the absolute value of val.
"""

def kdiff_pairs(nums,k):
	#get all the pairs
	if k < 0 :
		return 0
	numsSet, pairsSet = set(), set()
	
	for num1 in nums:
		for num2 in [num1 +k, num1-k]:
			if num2 in numsSet:
				pairsSet.add(tuple(sorted([num1,num2])))
		numsSet.add(num1)
	return len(pairsSet)


nums = [1,2,3,4,5]
k = 1
print(kdiff_pairs(nums,k))