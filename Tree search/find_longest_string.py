#!/bin/python

def find_longest_string(string):
    print string
    max_length = 0
    string_index = 0
    temp_string = ''

    for item in string:
        if item in temp_string:
            _index = temp_string.index(item)
            temp_string = temp_string[_index+1:]
            temp_string = temp_string + item
            #print temp_string
        else:
            temp_string = temp_string + item

        string_index = string_index + 1
        
        if len(temp_string) > max_length:
            tail_index = string_index
            head_index = string_index - len(temp_string)
            max_length = len(temp_string)
            print max_length
            print temp_string
    print head_index, tail_index
    print string[head_index:tail_index]

find_longest_string("1231231234848481238")
