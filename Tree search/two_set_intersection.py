#!/bin/python
import time

def two_set_intersection(first_list, second_list):
    '''notice index and value'''
    first_index = 0
    second_index = 0
    insection_list = []
    times = 0

    while first_index < len(first_list) and second_index < len(second_list):
        print times
        times = times + 1
    
        if first_list[first_index] == second_list[second_index]:
            print 'find equal: ', first_list[first_index]
            insection_list.append(first_list[first_index])
            first_index = first_index + 1
            second_index = second_index + 1
        elif first_list[first_index] < second_list[second_index]:
            print 'first index added...first is: ',first_index
            first_index = first_index + 1
        else:
            print 'second index added...second is: ',second_index
            second_index = second_index + 1
        
        time.sleep(1)
    print insection_list


first_list = [1, 2, 3, 5, 7, 9, 11, 33, 79, 110, 120, 130, 140, 150,160,170,180,190]
second_list = [1, 4, 6, 8, 9, 150, 151]

two_set_intersection(first_list, second_list)
