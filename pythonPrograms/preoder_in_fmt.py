'''
   pattern {{{ Input                      output
                a                         a
            b       c                     a b
          d   e  f    g                   a b d
                                          a b e
                                          a c
                                          a c f
                                          a c g
        sol: use preorder for traversing
'''

class node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

root = node('a')

v11 = root.left = node('b')
root.left.parent = root

v12 = root.right = node('c')
root.right.parent = root

v21 = root.left.left = node('d')
root.left.left.parent = v11

v22 = root.left.right = node('e')
root.left.right.parent = v11

v23 = root.right.left = node('f')
root.right.left.parent = v12

v24 = root.right.right = node('g')
root.right.right.parent = v12

def printPattern(root):
    if root!=None:
        print(printParent(root).strip())
        printPattern(root.left)
        printPattern(root.right)


def printParent(root):
    if root:
        return('' + printParent(root.parent) + ' ' + str(root.val))
    else:
        return ''

printPattern(root)

queue = []
def levelOrderTraverse(root):
    if root!=None:
        print(root.val)
        if(root.left):
            queue.append(root.left)
        if(root.right):
            queue.append(root.right)
        if(queue):
            nxt_ele = queue[0]
            queue.remove(nxt_ele)
            levelOrderTraverse(nxt_ele)

levelOrderTraverse(root)
