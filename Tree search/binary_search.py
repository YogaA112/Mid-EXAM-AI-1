#!/bin/python
'''
二分查找来实现根号n
'''

def binary_search(key):

    half_of_key = key/2.0
    old_half_of_key = half_of_key

    n = 2.0
    last_half_of_key = half_of_key
    while half_of_key * half_of_key != key:
        time.sleep(0.3)
        print half_of_key

        if half_of_key * half_of_key < key:
            half_of_key = half_of_key + old_half_of_key/n
        else:
            half_of_key = half_of_key - old_half_of_key/n
        n = n*2

        if half_of_key == last_half_of_key:
            break
        else:
            last_half_of_key = half_of_key


    print half_of_key


binary_search(26)
