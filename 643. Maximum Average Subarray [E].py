"""
You are given an integer array nums consisting of n elements, and an integer k.
Find a contiguous subarray whose length is equal to k that has the maximum average
 value and return this value. Any answer with a calculation error less than 10-5 will be accepted.
"""
def maximum_average(nums,k):
	#base case, if the length of the array is smaller than k
	if len(nums) <=k:
		return sum(nums)/k
	s = 0
	arr = []
	for i in range(len(nums)):
		print("nums[i] is:",nums[i])
	#create an s to add all the elements up to k
		if i < k:
			s += nums[i]
			print("1. added nums[i]",nums[i]," to s")	
	#then add the next element and remove the 	
		else:
			arr.append(s)
			s+=nums[i]
			#print("added", nums[i])
			#print("2. added nums[i]",nums[i]," to s")
			s-=nums[i-k]
			#print("subtracted",nums[i-k])
			#print("s is",s)
			arr.append(s)
			
		print("---")
	
	return max(arr)/k

#nums = [1,2,3,4]
#nums = [1,12,-5,-6,50,3] 
#nums = [0,4,0,3,2]
nums = [0,1,1,3,3]
k = 4
print(maximum_average(nums,k))