'''
Harris Walk of Ordered Binary Tree
traverse following order to obtain binary string
1=down, 0=up
'''

# pip install binarytree
from binarytree import Node, build
values = [1,2,3,4,None,6,7]
root = build(values)
print(root)


'''
As a starter, try with a list 
'''

def getStr(node,str): 
    if node.left :
        str.append(1)
        getStr(node.left,str)
    if node.right :
        str.append(1)
        getStr(node.right,str)
    str.append(0)
def getString(root,str) :
    getStr(root,str)
    while not str[-1] : # last bits are useless
        str.pop()

str = []
getString(root,str)
print(str)


def buildTree(node, str):
    # this stack should be shorter than tree height
    stack = [node] 
    cur = node
    while str : 
        down = str.pop(0)
        if down : 
            stack.append(cur)
            if cur.left : # had a left child
                cur.right = Node(0)
                cur = cur.right
            else : # no left child
                cur.left = Node(0)
                cur = cur.left
        else :
            cur = stack.pop()

new_root = Node(0)
buildTree(new_root,str)
print(new_root)


'''
Now, try with binary string as int
'''
def getBinStr(node,str): 
    if node.left :
        # str.append(1)
        str = 2*str + 1
        str = getBinStr(node.left,str)
    if node.right :
        # str.append(1)
        str = 2*str + 1
        str = getBinStr(node.right,str)
    # str.append(0)
    str *= 2
    return str
def getBinString(root,str) :
    str = getBinStr(root,str)
    while str%2 == 0:
        str /= 2
