'''
Your are given an array of positive integers nums.
Count and print the number of (contiguous) subarrays where the 
product of all the elements in the subarray is less than k.
'''

def arrProd(nums,k):
	for i in range(len(nums)):
		for j in range(i+1, len(nums)+1):
			print(prod(nums[i:j]))

nums = [10,5,2,6]
k = 100
print(arrProd(nums,k))