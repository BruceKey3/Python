class Node(object):
    value = 0;
    children = [];

    def __init__(self,value):
        self.value = value
        self.children = []

    def addChild(self, child):
        self.children.append(child)

def breadth_first_traversal(root):
    res = [[root]]
    breadth_first_helper(root,res,0)
    for i in res:
        for j in i:
            print(j.value)

def breadth_first_helper(node, acc, level):
    for i in node.children:
        if len(acc) <= level:
            acc.append([i])
        else:
            acc[level].append(i)
        breadth_first_helper(i,acc,level+1)

def depth_first_traversal(root):
    if(not root):
        return
    print(root.value)
    for i in root.children:
        depth_first_traversal(i)


child1 = Node(3)
child2 = Node(7)
child3 = Node(10)
child4 = Node(12)
child5 = Node(15)

child2.addChild(child3)
child1.addChild(child4)
child1.addChild(child5)

root = Node(5)
root.addChild(child1)
root.addChild(child2)
print("Depth first:")
depth_first_traversal(root)
print("Breadth first:")
breadth_first_traversal(root)

'''
    5
   / \
  3   7
 / \   \
12  15  10
'''
