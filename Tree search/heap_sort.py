#!/bin/python
import time
'''
堆排序
'''

def heap_sort(array):
    '''big stock'''
    sorted_array = []

    while array:
        not_leaf_node = (len(array) +1)/2 -1

        while not_leaf_node >= 0:

            _child_node_array = []
            if not_leaf_node*2 + 1 < len(array):
                node_left_leaf = not_leaf_node*2 + 1
                _child_node_array.append(node_left_leaf)
            if  not_leaf_node*2 + 2 < len(array):
                node_right_leaf = not_leaf_node*2 + 2
                _child_node_array.append(node_right_leaf)
            print 'left and right node is: ', _child_node_array


            for _node in _child_node_array:
                if array[not_leaf_node] < array[_node]:
                    _temp_node = array[not_leaf_node]
                    array[not_leaf_node] = array[_node]
                    array[_node] = _temp_node

            not_leaf_node = not_leaf_node - 1
            print 'array and branch: ', array, not_leaf_node
            time.sleep(1)

        big_item = array[0]
        print array, big_item
        time.sleep(1)
        del array[0]
        sorted_array.append(big_item)
    print sorted_array


array = [3, 5, 88, 90, 27, 1, 9, 4, 6, 7, 11, 19, 32, 59, 66]
heap_sort(array)
