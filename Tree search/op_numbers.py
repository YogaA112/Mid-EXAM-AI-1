#!/bin/python


def compute(arr):
    op_code_table = {
            "+": 1,
            "-": 1,
            "*": 2,
            "/": 2
            }

    op_stack =[]
    number_stack = []

    for item in arr:
        if item in op_code_table:
            if not op_stack:
                op_stack.append(item)

            elif op_code_table[op_stack[-1]] >= op_code_table[item]:
                op_code = op_stack.pop()
                op_stack.append(item)
                op_right_number = number_stack.pop()
                op_left_number = number_stack.pop()
                if op_code == '+':
                    result =  op_left_number - op_right_number
                    number_stack.append(result)
                elif op_code == "-":
                    result = op_left_number - op_right_number
                    number_stack.append(result)
                elif op_code == "*":
                    result = op_right_number * op_left_number
                    number_stack.append(result)
                elif op_code == "/":
                    result = op_left_number / op_right_number
                    number_stack.append(result)
                else:
                    print "ERROR"
                
            else:
                op_stack.append(item)
        else:
            number_stack.append(item)
        print number_stack, op_stack

    while op_stack:
        op_code = op_stack.pop()
        op_right_number = number_stack.pop()
        op_left_number = number_stack.pop()
        print op_left_number, op_code, op_right_number
        if op_code == '+':
            result =  op_left_number + op_right_number
            number_stack.append(result)
        elif op_code == "-":
            result = op_left_number - op_right_number
            number_stack.append(result)
        elif op_code == "*":
            result = op_right_number * op_left_number
            number_stack.append(result)
        elif op_code == "/":
            result = op_left_number / op_right_number
            number_stack.append(result)
        else:
            print "ERROR"
    return number_stack[0]
    print number_stack[0], op_stack

def spilit_brackets(arr):
    item_stack = []
    temp_stack = []
    for item in arr:
        if item == ')':
            while item_stack[-1] != '(':
                temp_stack.append(item_stack.pop())
            item_stack.pop()
            result =  compute(temp_stack)
            item_stack.append(result)
            temp_stack = []
        else:
            item_stack.append(item)
    print item_stack
    result = compute(item_stack)
    print result
    
compute([100, '+', 200, '*', 200, '/', 10, '/', 2])
spilit_brackets(['(','(', 1, '+', 2, ')', '+', 3, ')', '+', 11, '/', 1])
