#!/bin/python
import time

def quic_sort(array, begin_point, end_point):
    base = array[end_point]
    init_begin = begin_point
    init_end = end_point
    #time.sleep(1)

    while begin_point < end_point and end_point >=0:
        while begin_point < end_point:
            #time.sleep(1)
            print 'left array: ', array, 'base is: ', base, 'begin point is: ', begin_point
            if array[begin_point] > base:
                array[end_point] = array[begin_point]
                break
            else:
                begin_point = begin_point + 1

        while end_point > begin_point:
            #time.sleep(1)
            print 'right array: ',array
            if array[end_point] < base:
                array[begin_point] = array[end_point]
                break
            else:
                end_point = end_point - 1

    print 'finished, begin end point are: ', begin_point, end_point
    array[begin_point] = base


    if init_begin <  begin_point - 1:
        quic_sort(array, init_begin, begin_point - 1 )
    if end_point + 1 < init_end:
        quic_sort(array, end_point + 1, init_end)
    print array

array = [3, 5, 1, 9, 4, 6, 7, 11, 100, 30, 21, 0, 8]
array = [20975,
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
end = len(array)

quic_sort(array, 0, end -1)

