class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def insert (root,key):
    if root is None: 
        return Node(key)
    else: 
        if root.data==key:
            return root
        elif root.data>key:
            root.left=insert(root.left,key)
        else:
            root.right=insert(root.right,key)
    return root
def inorder (root):
    if root is None:
        return
    inorder(root.left)
    print (root.data, end='->')
    inorder(root.right)
def preorder (root):
    if root is None:
        return
    print (root.data,end='->')
    preorder(root.left)
    preorder(root.right)
def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data,end='->')
root=Node(50)
insert(root,10)
insert(root,20)
insert(root,40)
insert(root,25)
insert(root,55)
insert(root,45)
insert(root,75)
insert(root,85)
insert(root,65)
insert(root,35)
insert(root,10)
insert(root,60)
insert (root,70)
insert(root,30)
insert(root,80)
print ('inorder:')
inorder(root)
print('\npreorder:')
preorder(root)
print('\npostorder:')
postorder(root)