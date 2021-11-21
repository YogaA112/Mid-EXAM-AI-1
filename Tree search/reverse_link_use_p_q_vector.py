#!/bin/python


class ListNode():
    def __init__(self, value):
        self.value = value
        self.next = None

head = ListNode(100)
array = [1,2,3,4,5]
tail = ListNode(200)
head.next = tail

print head.value, array, tail.value

while array:
    temp_node = ListNode(array.pop())
    temp_node.next = head.next
    head.next = temp_node


p_node = head
if p_node.next:
    temp_node = p_node.next
    p_node.next = None
    if temp_node.next:
        q_node = temp_node.next
        temp_node.next = None
    else:
        p_node.next = None
        temp_node.next = p_node
       
    print temp_node
else:
    print p_node

#print p_node.value, temp_node.value, q_node.value

while q_node:
    temp_node.next = p_node
    p_node = temp_node
    temp_node = q_node
    q_node = q_node.next
    temp_node.next = None

temp_node.next = p_node

print p_node.value, temp_node.value

while temp_node:
    print temp_node.value
    temp_node = temp_node.next



