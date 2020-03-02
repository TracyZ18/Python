# store binary tree as binary string
# preorder; depend on children, assign 00,01,10,11

from binarytree import Node, build
values = [1,2,4,3,None,None,None,None,5,None,None,None,None,None,None,None,None,6,7]
root = build(values)
# print(root)

'''
As a starter, try with a list 
'''

# convert to binary "string"
# (using list for now to get the feel of it)
def getString(node, str) :
    if node:
        if node.left:
            str.append(1) # str*2 + 1
        else:
            str.append(0) # str*2 + 0
        if node.right:
            str.append(1)
        else:
            str.append(0)
        getString(node.left, str)
        getString(node.right, str)

# str = []
# getString(root,str)
# print(str)

# recursive call!
def buildTree(node, str):
    # set up root and its children
    val = (str.pop(0),str.pop(0)) 
    if val[0] == 1 :
        node.left = Node(0)
        buildTree(node.left, str)
    if val[1] == 1 :
        node.right = Node(0)
        buildTree(node.right, str)

# new_root = Node(0)
# buildTree(new_root,str)
# print(new_root)
# print(root)

'''
Now, try with binary string as int
'''

def getBinString(node, str) :
    if node:
        if node.left:
            str = str*2 + 1
        else:
            str = str*2 + 0
        if node.right:
            str = str*2 + 1
        else:
            str = str*2 + 0
        tmp = getBinString(node.left, str)
        if tmp :
            str = tmp
        tmp = getBinString(node.right, str)
        if tmp :
            str = tmp
        return str

# bin_str = 0
# bin_str = getBinString(root, bin_str)
# print(bin_str)

'''
def firstBit(num):
    k = 2**m.floor(m.log2(num))
    return k

# print(5&firstBit(5))
# problem: first bit will always be true...


# problem: prev was 01 or 00, start with 01 (odd power of 2) or 00 (gap)
# first idea: check old string power, chop off first two bit, check power
def leadingBits(num, zero):
    k = m.floor(m.log2(num)) # note highest powers
    if k%2 == 1 : #  prev was 01
        k += 1
    if zero : # prev was 00
        k += 2
    # too hard

# solution: just use k as counter
# initialize with m.floor(m.log2(str)) to even
'''

import math as m

def buildBinTree(node,str) :
    pow = int(m.floor(m.log2(str)))
    stack = [node] # start with only root node
    while pow != -1 :
        left = (2**pow)&str # check first bit 
        str -= 2**pow # go to next bit
        pow -= 1

        right = (2**pow)&str # check second bit
        str -= 2**pow
        pow -= 1

        # stack one by one
        cur = stack.pop()
        if right : # right first, because want to peak left first
            cur.right = Node(0)
            stack.append(cur.right)
        if left :
            cur.left = Node(0)
            stack.append(cur.left)

# new_root = Node(0)
# buildBinTree(new_root,bin_str)
# print(new_root)
# print(root)


'''
Demonstration of the results
'''
print(root)

# list implementation
bin_list = []
list_root = Node(0)
getString(root, bin_list)
buildTree(list_root, bin_list)
print(list_root)

# int implementation
int_root = Node(0)
bin_int = getBinString(root, 0)
buildBinTree(int_root, bin_int)
print(int_root)


'''
RECURSION IN ASSEMBLY
(wasn't useful here, but anyways :P)
- before call, stack params
- unstack params, put in vars
- do stuff with vars
    - if base case
        - stack the return value
        - jr (returned to previous function)
    - otherwise
        - stack recursion params
        - jal (recursion call)
        - unstack return value
        - do stuff with return value
        - return final value
'''