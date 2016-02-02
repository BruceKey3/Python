# Class for a node, holds a value and the children
class Node(object):
    value = 0;
    children = [];

    def __init__(self,value):
        self.value = value
        self.children = []

    def addChild(self, child):
        self.children.append(child)

        
#breadth first functions

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


# depth first functions

# Helper functions for depth first

def isNone(x):
    return (not (x is None))

def compare_item(root, item):
    if root.value == item:
       return root

def check_list( node, i, path):
    if not (node is None):
        path.append(i)
        return node
    
# actual functions for depth first
def depth_first_traversal(root):
    # print the node's value
    f = lambda *x : print(x[0].value)
    # do nothing
    g = lambda *args: None
    depth_first_search_helper(root, [], None, f, g)
    
def depth_first_search(root, item):
    path = []
    depth_first_search_helper(root, path, item, compare_item, check_list)
    path.append(root)
    path.reverse()
    return path

'''
 Helper function for all depth first algorithms.
 It runs a basecase function before the loop passing in the root and item
 and returns the result if there is one.
 Also runs a recursive_case function after every iteration in the loop passing
 it the result of the recursive call, the child and the path so far.
 If this recursive_case has a result, it returns it.
'''
def depth_first_search_helper(root, path, item, basecase, recursive_case):
    if not root:
        return None
    res = basecase(root, item)
    if isNone(res) :
        return res
    for i in root.children:
        node = depth_first_search_helper(i,path,item, basecase, recursive_case)
        res = recursive_case(node,i, path)
        if isNone(res) :
            return res


# main

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

print("Depth first path to 15:")
path = depth_first_search(root,15)

for i in path:
    print(i.value)


'''
    5
   / \
  3   7
 / \   \
12  15  10
'''
