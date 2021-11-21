#-*-coding: utf-8-*-
#!/bin/python

'''寻找第k大的数'''
'''现在只实现了奇数层面的第k大但是偶数报错'''
'''时间复杂度为nlogn'''

def find_medium_key(array, head_index, tail_index):
    
    if not array:
        return

    if len(array) %2 == 1:
        print 'odd number of array...'
        _middle_of_array_index = len(array) /2
    else:
        _middle_of_array_index = len(array) -1 /2
    
    _base_item = array[tail_index]

    _head_index = head_index
    _tail_index = tail_index

    while _head_index < _tail_index:
        while _head_index < _tail_index:
            if array[_head_index] > _base_item:
                array[_tail_index] = array[_head_index]
                break
            else:
                _head_index = _head_index + 1
        while _head_index < _tail_index and _tail_index >=0:
            if array[_tail_index] < _base_item:
                array[_head_index] = array[_tail_index]
                break
            else:
                _tail_index = _tail_index - 1
    array[_head_index] = _base_item


    if _head_index > _middle_of_array_index:
        find_medium_key(array, head_index, _head_index)
    elif _head_index < _middle_of_array_index:
        find_medium_key(array, _head_index, tail_index)
    elif _head_index == _middle_of_array_index:
        print array[_head_index]
        return array[_head_index]
    else:
        print 'error'
        return 'error'
    

array = [5,2,3,6,9,14,4,
        83,
        24,
        8,
        30,
        74,
        67,
        88,
        93,
        57,1]
find_medium_key(array, 0, len(array)-1)
