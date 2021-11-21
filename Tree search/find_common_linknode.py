#!/bin/python
import time

def find_common_linknode(list1, list2):
    list1_dict = {}
    list2_dict = {}

    while list1:
        list1_dict[list1] = 0
        list1 = list1.next
    while list2:
        if list2 in list1_dict:
            print 'cross node...', list2, list2.value
            break
        else:
            print list2.value
            list2 = list2.next


class linkNode():
    def __init__(self, value):
        self.value = value
        self.next = None


list1 = linkNode(100)
list2 = linkNode(200)

array = [1,3,4,3,5,6,7,8,9,10]

while array:
    item = array.pop()
    temp_node = linkNode(item)
    temp_node.next = list1.next
    list1.next = temp_node

list2_next = linkNode(300)
list2_next_next = linkNode(400)

list2.next = list2_next
list2_next.next = list2_next_next
list2_next_next.next = list1.next.next.next

array2 = [1,2,3]
list3 = linkNode(300)

while array2:
    item = array2.pop()
    temp_node = linkNode(item)
    temp_node.next = list3.next
    list3.next = temp_node

list3.next.next.next.next = list3

while list3:
    print list3.value, list3
    list3 = list3.next
    time.sleep(1)


find_common_linknode(list1, list2)
