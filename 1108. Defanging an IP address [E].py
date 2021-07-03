"""
Given a valid (IPv4) IP address, return a defanged version of that IP address.
A defanged IP address replaces every period "." with "[.]".
"""

def defanging_IPaddress(address):
	answer = ""
	for i in range(len(address)):
		if address[i] == ".":
			answer +="[.]"
		else:
			answer+=address[i]
	return answer

address = "1.1.1.1"
print(defanging_IPaddress(address))