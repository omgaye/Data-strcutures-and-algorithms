class Node:
	def __init__(self,key):
		self.left = None
		self.right = None
		self.val = key

def insert(root,node):
	if root is None:
		root = node
	else:
		if root.val < node.val:
			if root.right is None:
				root.right = node
			else:
				insert(root.right, node)
		else:
			if root.left is None:
				root.left = node
			else:
				insert(root.left, node)

def inorder(root):
	if root:
		inorder(root.left)
		print(root.val)
		inorder(root.right)

r = Node(5)
a=input("enter the elements :")
insert(r,Node(a))
b=input("enter the elements :")
insert(r,Node(b))
c=input("enter the elements :")
insert(r,Node(c))
d=input("enter the elements :")
insert(r,Node(d))
e=input("enter the elements :")
insert(r,Node(e))
f=input("enter the elements :")
insert(r,Node(f))

inorder(r)
