#!/bin/python


class biTree():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


root = biTree(50)
array = [1,2,3,4,5,6,7]

for item in array:
    temp_tree = biTree(item)
    if item % 2 == 0:
        temp_tree.right = root.right
        root.right = temp_tree
    else:
        temp_tree.left = root.left
        root.left = temp_tree

temp_tree_add_1 = biTree(17)
temp_tree_add_2 = biTree(16)
root.left.right = temp_tree_add_1
root.right.left = temp_tree_add_2


tree_stack = []
temp_tree = root
tree_stack.append(temp_tree)

while tree_stack :
    signal = False
    temp_tree = tree_stack.pop()
    print '\n--------new turn-------'
    print temp_tree.value, 'root node...'
    if temp_tree.right != None:
        print temp_tree.right.value, 'right node...'
        tree_stack.insert(0, temp_tree.right)
    else:
        print 'left child is null...'
    if temp_tree.left != None:
        print temp_tree.left.value, 'left node...'
        tree_stack.insert(0, temp_tree.left)
    else:
        print 'right child is null...'
    #temp_tree = tree_stack.pop() #!!!!!!cannot be there!!!!!, last node will be ignored...  


#print tree_stack
#print temp_tree.left.value


