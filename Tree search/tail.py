#!/bin/python

'''
display end line of the file
'''
filename = '/root/shuabao-web-api-transfer-data-test.txt'
line = 5

with open(filename) as openfile:
    i = 1
    openfile.seek(0, 2)
    while len(openfile.readlines()) <= line:
        i = i * 2
        openfile.seek(-i, 2)
        print i

    openfile.seek(-i, 2)

    tail_info = openfile.readlines()[-line:]
    
    for items in tail_info:
        print items
    print openfile.tell()

openfile.close()

