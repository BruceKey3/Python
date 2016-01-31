class Node(object):
    value = 0;
    children = [];

    def __init__(self,value,child=None):
        self.value = value
        self.children = [child]

    def addChild(self, child):
        self.children.append(child)

def breadth_first(root):
    res = []
    breadth_first_helper(root,res,0)

def breadth_first_helper(node, acc, level):
    return;
    for i in root.children:
        breadth_first_helper(i,acc,level+1)
      

def depth_first(root):
    if(not root):
        return
    print(root.value)
    for i in root.children:
        depth_first(i)


child1 = Node(3,[])
child2 = Node(7,[])
child3 = Node(10,[])
child4 = Node(12, [])
child5 = Node(15, [])

child2.addChild(child3)
child1.addChild(child4)
child1.addChild(child5)

root = Node(5, child1)
root.addChild(child2)
print("Depth first:")
depth_first(root)
print("Breadth first:")
breadth_first(root)

'''
    5
   / \
  3   7
 / \   \
12  15  10
'''
