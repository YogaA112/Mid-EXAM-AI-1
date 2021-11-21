#!/bin/python
import threading


signal = 'even'

def print_odd():
    _index = 1
    global signal
    max_value = 10
    while _index < max_value:
        if signal == 'odd':
            print _index
            _index = _index + 2
            signal = 'even'
        else:
            pass


def print_even():
    _index = 0
    global signal
    max_value = 10
    while _index < max_value:
        if signal == 'even':
            print _index
            _index = _index + 2
            signal = 'odd'
        else:
            pass

t1 = threading.Thread(target=print_odd)
t2 = threading.Thread(target=print_even)
t1.start()
t2.start()

