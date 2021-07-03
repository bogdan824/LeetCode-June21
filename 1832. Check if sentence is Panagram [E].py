"""
A pangram is a sentence where every letter of the English alphabet appears at least once.
Given a string sentence containing only lowercase English letters, 
return true if sentence is a pangram, or false otherwise.
"""

def is_Panagram(sentence):
	s = set(sentence)
	if len(s) == 26:
		return True 
	return False

sentence = "abccc"
#sentence = "thequickbrownfoxjumpsoverthelazydog"
print(is_Panagram(sentence))

"""
hashm = {"a":"0","b":"0","c":"0","d":"0","e":"0","f":"0","g":"0","h":"0","i":"0","j":"0","k":"0","l":"0","m":"0","n":"0","o":"0","p":"0","q":"0","r":"0","s":"0","t":"0","u":"0","v":"0","w":"0","x":"0","y":"0","z":"0"}

	for i in range(len(sentence)):
		if sentence[i] in hashm:
			hashm[sentence[i]]+=1
	for k,v in hashm.items():
		print(k,v)
"""