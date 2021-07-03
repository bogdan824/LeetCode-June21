'''
There are several cards arranged in a row, and each card has an associated number
of points The points are given in the integer array cardPoints.
In one step, you can take one card from the beginning or from the end of the row.
You have to take exactly k cards.
Your score is the sum of the points of the cards you have taken.
Given the integer array cardPoints and the integer k, return the maximum score you can obtain.
'''

def maxScore(cardPoints,k):
	best = score = sum(cardPoints[:3])
	
	for i in range(1,k+1):
		#print("score",score)
		score = score - cardPoints[k-i] + cardPoints[-i]
		
		#print("cardPoints[k-i]", cardPoints[k-i])
		#print("cardPoints[-i]",cardPoints[-i])
		#print("cardPoints[k-i] + cardPoints[-i]",cardPoints[k-i] + cardPoints[-i])
		best = max(best,score)
		#print("---")
	return best
		

#cardPoints = [5,4,-1,4,2,-2,1,6]	
cardPoints = [1,2,3,4,5,6,1] #k=3
#cardPoints = [100,40,17,9,73,75] #k=3
k = 3
print(maxScore(cardPoints,k))



"""
#1st approach - not working
i = 0
	j = len(cardPoints)
	x = j
	maxi = 0
	
	while k >= 0:
		suma = sum(cardPoints[0:k]) + sum(cardPoints[x:j])
		print(suma)
		k-=1
		x-=1
		if suma > maxi:
			maxi = suma
	return maxi
"""
