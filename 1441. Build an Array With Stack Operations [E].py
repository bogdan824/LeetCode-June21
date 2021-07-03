"""
Given an array target and an integer n. In each iteration, you will read a number from  list = {1,2,3..., n}.

Build the target array using the following operations:

Push: Read a new element from the beginning list, and push it in the array.
Pop: delete the last element of the array.
If the target array is already built, stop reading more elements.
Return the operations to build the target array. You are guaranteed that the answer is unique.
"""

def array_wStack_op(target,n):
	answer = []
	for i in range(1,n+1):
		if i<= target[-1]:
			answer.append("Push")
			if i not in target:
				answer.append("Pop")
		else:
			return answer
	return answer

target = [1,3]
n = 3
print(array_wStack_op(target,n))