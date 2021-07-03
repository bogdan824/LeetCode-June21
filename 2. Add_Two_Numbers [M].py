'''
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''
class Node:	
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

ls1 = Node(2,None)
ls1.next = Node(4,None)
ls1.next.next = Node(3,None)

ls2 = Node(5,None)
ls2.next = Node(6,None)
ls2.next.next = Node(4,None)