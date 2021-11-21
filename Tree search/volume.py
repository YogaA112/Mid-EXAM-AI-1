#!/bin/python


arr = [1,2,3,4,6]
new_list = [3,5,6,7,9]

arr_length = len(arr) -1
new_list_length = len(new_list) -1

arr_index = arr_length /2
new_list_index = new_list_length /2

while arr_index != new_list_index:
    if arr[arr_index] > new_list[new_list_index]:
        
