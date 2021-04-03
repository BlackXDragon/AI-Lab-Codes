class node:
    def __init__(self, data):
        self.data=data;
    def left_child(self,lc):
        assert lc.data<self.data
        self.left=lc
    def right_child(seld,rc):
        assert rc.data>self.data
        self.right=rc

arr=eval(input("Enter BST data: "))

root=node(arr[0])


def add_node(n,e):
    if e<n.data:
        if not n.left:
            n.left(node(e))
        else:
            add_node(n.left,e)
    else:
        if not n.right:
            n.right(node(e))
        else:
            add_node(n.right,e)

for i in range(len(arr)):
    add_element(root,i)

def print_tree(root):
    print(root.data)
    
