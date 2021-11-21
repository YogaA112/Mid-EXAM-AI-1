#!/bin/python

odd_value = 0
even_value = 0
max_value = 10

def print_odd(max_value, odd_value, even_value):
    if odd_value > max_value:
        return
    if odd_value < even_value:
        print odd_value, '-----'
        print_even(max_value, odd_value +2, even_value)

def print_even(max_value, odd_value, even_value):
    if even_value > max_value:
        return
    if odd_value > even_value:
        print even_value, '|||||'
        print_odd(max_value, odd_value, even_value + 2)


print_even(max_value, 1, 0)

