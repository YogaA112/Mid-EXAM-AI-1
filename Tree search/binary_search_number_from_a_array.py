#!/bin/python



def find_medium_number(array, number):
    pre_index = 0
    tail_index = len(array) -1
    
    target_index = (pre_index + tail_index ) /2
    
    while pre_index <= tail_index:
        if array[target_index] > number:
            tail_index = target_index -1
            target_index = (pre_index + tail_index ) /2
        elif array[target_index] < number:
            pre_index = target_index +1
            target_index = (pre_index + tail_index ) /2
        elif array[target_index] == number:
            print number, target_index
            return
    
    print 'not found...'



find_medium_number([1,2,3,4,5,6,7,8,9,10],3)
    
