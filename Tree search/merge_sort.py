#!/bin/python



def quic_sort(array, head_index, tail_index):
    _head_index = head_index
    _tail_index = tail_index
    _base_item = array[tail_index]
    while _head_index < _tail_index:
        while _head_index < _tail_index:
            if array[_head_index ] > _base_item:
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

    if _head_index -1 > head_index:
        quic_sort(array, head_index, _head_index -1)
    if _tail_index +1 < tail_index:
        quic_sort(array, _tail_index + 1, tail_index)
    #print array
    return array


def merge_two_array(left_array, right_array):
    _left_index = 0
    _right_index = 0

    _left_array_max_index = len(left_array) -1
    _right_array_max_index = len(right_array) -1

    array = []

    while _left_index <= _left_array_max_index and _right_index <= _right_array_max_index:
        if left_array[_left_index] > right_array[_right_index]:
            array.append(right_array[_right_index])
            _right_index = _right_index + 1
        elif left_array[_left_index] < right_array[_right_index]:
            array.append(left_array[_left_index])
            _left_index = _left_index +1
        else:
            array.append(left_array[_left_index])
            _right_index = _right_index + 1
            _left_index = _left_index +1

    if _left_index <= _left_array_max_index:
        array.extend(left_array[_left_index:])
    if _right_index <= _right_array_max_index:
        array.extend(right_array[_right_index:])
    print left_array, right_array, array
    return array


def merge_sort(array, max_length):
    if len(array) > max_length:
        middle_index = len(array) /2
        left_array = array[:middle_index]
        right_array = array[middle_index:]
        left_array = merge_sort(left_array, max_length)
        right_array = merge_sort(right_array, max_length)

        array = merge_two_array(left_array, right_array)
        print array
        return array
    else:
        array = quic_sort(array, 0, len(array)-1)
        return array



merge_sort([9,8,7,6,1,3,5,2,4,12,15,91,82,53], 3)
