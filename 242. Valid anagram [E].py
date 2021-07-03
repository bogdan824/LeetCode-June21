"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
"""

def valid_anagram(s,t):
	s = list(s)
	t = list(t)
	s.sort()
	t.sort()

	return s == t

s = "anagram"
t = "nagaram"
print(valid_anagram(s,t))