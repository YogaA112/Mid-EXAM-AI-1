#!/bin/python
import time

def max_length_not_repeated_string(array):
    temp_array = []
    max_length = 0
    head_index = 0
    tail_index = 0

    index = 0
    for item in array:
        if item not in temp_array:
            temp_array.append(item)
        else:
            _index = temp_array.index(item)
            temp_array.append(item)
            temp_array = temp_array[_index +1 :]

        if len(temp_array) > max_length:
            head_index = index - len(temp_array) +1
            tail_index = index
            max_length = len(temp_array)

        index = index + 1
        time.sleep(1)
        print temp_array, head_index, tail_index
    print temp_array, head_index, tail_index, array[head_index:tail_index]

array = [0,2,3,4,1,2,3,5,6,2,1, 1,1]
max_length_not_repeated_string(array)
