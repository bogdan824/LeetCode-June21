"""
You own a Goal Parser that can interpret a string command. The command consists of 
an alphabet of "G", "()" and/or "(al)" in some order. The Goal Parser will interpret 
"G" as the string "G", "()" as the string "o", and "(al)" as the string "al". 
The interpreted strings are then concatenated in the original order.
Given the string command, return the Goal Parser's interpretation of command.
"""
#straight away method: if-else.
#Alternative: hash map
def goal_parser(command):
	i = 0
	answer = ""
	while i < len(command):
		if command[i] == "G":
			answer+="G"
			i+=1
		elif command[i] == "(" and command[i+1] == "a":
			answer+="al"
			i+=4
		else:
			answer+="o"
			i+=2
	return answer


command = "G()(al)"
print(goal_parser(command))