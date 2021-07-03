'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.
'''
def groupAnagrams(strs):
	strs.sort()
	
	print(strs)


strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))