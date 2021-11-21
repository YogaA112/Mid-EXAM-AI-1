#!/bin/python


def frog_jump(number):
    
    index = 3

    odd_index_value = 1
    even_index_value = 2

    while index >= 3 and index < number:
        if index %2 ==0:
            odd_index_value = odd_index_value + even_index_value
        else:
            even_index_value = odd_index_value + even_index_value

        index = index +1
    print odd_index_value + even_index_value

frog_jump(34)
