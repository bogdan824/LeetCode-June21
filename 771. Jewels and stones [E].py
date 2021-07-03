"""
You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. 
You want to know how many of the stones you have are also jewels.
Letters are case sensitive, so "a" is considered a different type of stone from "A"
"""

def jewels_stones(jewels,stones):
	#get a variable answer that will keep track of appereance of any stone
	answer = 0
	#convert the list of jewls intoa a list so it can be easier to search through
	keep = list(jewels)
	for i in range(len(stones)):
		if stones[i] in keep:
			answer += 1
	return answer


jewels = "z"
stones = "ZZ"
print(jewels_stones(jewels,stones))