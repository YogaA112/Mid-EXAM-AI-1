#!/bin/python


class linkNode():
    def __init__(self, value):
        self.value = value
        self.next = None

first_list_head = linkNode(4)
second_list_head = linkNode(6)

first_array = [9, 9, 9, 8, 8]
second_array = [9, 9, 9, 9, 8]
print first_list_head.value, first_array
print second_list_head.value, second_array

while first_array:
    temp_link_node = linkNode(first_array.pop())
    temp_link_node.next = first_list_head.next
    first_list_head.next = temp_link_node

while second_array:
    temp_link_node = linkNode(second_array.pop())
    temp_link_node.next = second_list_head.next
    second_list_head.next = temp_link_node


pre_carry = 0
first_stack = []
second_stack = []
result_array = []

while first_list_head is not None:
    first_stack.append(first_list_head.value)
    first_list_head = first_list_head.next

while second_list_head is not None:
    second_stack.append(second_list_head.value)
    second_list_head = second_list_head.next

while first_stack and second_stack:
    first_node = first_stack.pop()
    second_node = second_stack.pop()
    result = first_node + second_node + pre_carry
    print first_node,'+', second_node,'=',result,'result'
    pre_carry = result / 10
    result = result % 10
    result_array.insert(0,result)

while not first_stack and second_stack:
    result = second_stack.pop() + pre_carry
    pre_carry = result / 10
    result = result % 10
    result_array.insert(0,result)

while not second_stack and first_stack:
    result = second_stack.pop() + pre_carry
    pre_carry = result / 10
    result = result % 10
    result_array.insert(0,result)

if pre_carry:
    result_array.insert(0, pre_carry)

print result_array

