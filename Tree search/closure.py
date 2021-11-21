#!/bin/python3
#-*-coding: utf-8-*-

def make_closure(step): #包装器
    num = 10
    def have_fun(): #内部函数
        nonlocal num
        num = num + step
        print(num)
    return have_fun



step_echo = make_closure(3)
times = 1
while times < 10:
    times = times + 1
    step_echo()
