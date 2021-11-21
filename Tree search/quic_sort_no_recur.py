#!/bin/python


def quic_sort_no_recur(array):
    stack = []
    signal = True
    while stack or signal:
        signal = False

        if not stack:
            _base_item = array[-1]
            print _base_item, 'base'
            _head_index = 0
            _tail_index = len(array) -1

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
            print array, 'array'
            if 0 < _head_index -1:
                stack.append([0,_head_index -1])

            if _head_index +1 < len(array) -1:
                stack.append([_head_index +1, len(array) -1])
            print _head_index,'index', stack, array

        else:
            index = stack.pop()
            tail_index = index[1]
            head_index = index[0]
            _tail_index = tail_index
            _head_index = head_index
            _base_item = array[tail_index]
            
            print '----',_base_item, 'base', head_index, _head_index, _tail_index, tail_index
            while _head_index < _tail_index:
                while _head_index < _tail_index:
                    if array[_head_index] > _base_item:
                        array[_tail_index] = array[_head_index]
                        break
                    else:
                        _head_index = _head_index + 1
                while _head_index < tail_index and _tail_index >=0:
                    if array[_tail_index] < _base_item:
                        array[_head_index] = array[_tail_index]
                        break
                    else:
                        _tail_index = _tail_index - 1

            array[_head_index] = _base_item

            print head_index, _head_index-1, _tail_index+1, tail_index
            if _head_index -1 > head_index:
                stack.append([head_index, _head_index -1])
            if _tail_index + 1 < tail_index:
                stack.append([_tail_index + 1, tail_index])
            print stack, array
    print array

quic_sort_no_recur([2,4,17,6,9,21,7,16,3,18,1,19,0,5,12,10])
