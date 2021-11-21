#!/bin/python
import time

class biTree():
    def __init__ (self, data):
        self.data = data
        self.left = None
        self.right = None


bi_tree = biTree(10)
bi_tree.left = biTree(9)
bi_tree.right = biTree(11)

bi_tree.left.left = biTree(13)
bi_tree.left.right = biTree(15)

bi_tree.right.left = biTree(17)
bi_tree.right.right = biTree(19)

bi_tree.right.right.left = biTree(25)
bi_tree.right.right.right = biTree(29)

bi_tree.right.right.left.left = biTree(30)
bi_tree.right.right.left.right = biTree(31)


search_bi_tree = bi_tree
bi_tree_stack = []

'''
## root -> left -> right

while search_bi_tree != None or bi_tree_stack != None:
    #print bi_tree_stack
    time.sleep(0.2)
    if search_bi_tree != None:
        print 'central node is: ', search_bi_tree.data
        bi_tree_stack.append(search_bi_tree)
        search_bi_tree = search_bi_tree.left

    else:
        if bi_tree_stack:
            search_bi_tree = bi_tree_stack.pop()
            search_bi_tree = search_bi_tree.right
        else:
            break
'''
reserved = {}

## left->root->right 
## when pops then print
## create a dict !!!

while search_bi_tree != None or bi_tree_stack != []:
    time.sleep(1)
    print 'begin..'
    #print reserved, bi_tree_stack
    
    while search_bi_tree != None and not reserved.has_key(search_bi_tree):
        bi_tree_stack.append(search_bi_tree)
        reserved[search_bi_tree] = 1
        #print search_bi_tree.data #, 'pushed'
        search_bi_tree = search_bi_tree.left

    if search_bi_tree:
        if search_bi_tree.right != None:
            search_bi_tree = search_bi_tree.right
            #print search_bi_tree.data, 'right node'
        else:
            if bi_tree_stack:
                search_bi_tree = bi_tree_stack.pop()
                print search_bi_tree.data
            else:
                break
    else:
        if bi_tree_stack:
            search_bi_tree = bi_tree_stack.pop()
            print search_bi_tree.data
        else:
            break
    
'''
## recursively root -> left -> right
def searchBiTree(search_bi_tree):
    while search_bi_tree != None:
        print search_bi_tree.data
        searchBiTree(search_bi_tree.left)
        searchBiTree(search_bi_tree.right)
        break

searchBiTree(search_bi_tree)
'''



'''
print bi_tree.left.left
print bi_tree.left.data
print bi_tree.left.right
'''

