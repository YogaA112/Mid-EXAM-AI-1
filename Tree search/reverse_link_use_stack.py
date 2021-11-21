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

node_stack = []


while head:
    node_stack.append(head)
    head = head.next

tail = node_stack.pop()
new_tail = tail

while node_stack:
    temp_node = node_stack.pop()
    tail.next = temp_node
    tail = tail.next
tail.next = None

print new_tail.value, tail.value

print '-------reverse-----'
while new_tail:
    print new_tail.value
    new_tail = new_tail.next

