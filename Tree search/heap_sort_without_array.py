#!/bin/python
import time

def heap_sort(array, index):
    if index <= 0:
        print array
        return

    last_branch_node_index = ( index+1 )/2 -1
    print 'last branch node is: ', last_branch_node_index

    _index = last_branch_node_index
    while _index < index and _index >= 0:
        print array, _index
        #time.sleep(0.2)
        _left_child_node_index = 2 * _index + 1
        _right_child_node_index = 2 * _index + 2
        _child_node = []
        if _left_child_node_index <= index:
            _child_node.append(_left_child_node_index)
        if _right_child_node_index <= index:
            _child_node.append(_right_child_node_index)
        
        for item in _child_node:
            if array[item] < array[_index]:
                temp_node = array[item]
                array[item] = array[_index]
                array[_index] = temp_node

        _index = _index - 1 
    
    temp_node = array[0]
    array[0] = array[index]
    array[index] = temp_node

    stock_sort(array, index - 1)

array=[8, 9, 11, 13, 19, 10, 3, 5, 6, 2, 1, 7, 4]
array=[20975,
        11323,
        4704,
        1828,
        31912,
        13648,
        19093,
        7485,
        17272,
        7510,
        11977,
        11240,
        11746,
        27985,
        28370,
        12423,
        1389,
        25432,
        19127,
        24294,
        30331,
        14280,
        26321,
        21765,
        15835,
        32118,
        20233,
        3788,
        6050,
        12760,
        27757,
        3075,
        15988,
        27576,
        1304,
        30016,
        20134,
        6470,
        20428,
        1747]
heap_sort(array, len(array)-1)
