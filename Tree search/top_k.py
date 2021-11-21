#!/bin/python
import time


def topk(array, k):
    k_array = []
    print array, k
    if not array:
        return 'error, array is null...'
    k_array.append(array[0])
    
    big_index = 1
    for item in array[1:]:

        index = 0
        time.sleep(1)

        while index < len(k_array):
            print k_array, index
            if item > k_array[index]:
                if index == len(k_array) -1:
                    k_array.append(item)
                    k_array = k_array[:k]
                    break
                elif index < len(k_array) -1:
                    index = index + 1
                else:
                    print 'index out of range...'
                    break
            else:
                k_array.insert(index , item)
                k_array = k_array[:k]
                break

    print k_array


array = [31302 , 12701 , 25865 , 20192 , 2911 , 17316 , 18760 , 5796 , 10866 , 22780 , 6166 , 24703 , 27223 , 8916 , 13875 , 994 , 27898 , 7256 , 26127 , 26959]
k = 3

topk(array, k)

