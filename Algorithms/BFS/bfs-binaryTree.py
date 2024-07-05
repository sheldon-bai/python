class TreeNode:
    def __init__(self, val=0, left=None, right=None, isTreasure=False):
        self.val = val
        self.left = left
        self.right = right
        self.isTreasure = isTreasure

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4, isTreasure=True)

def bfs(root):
    if root is None:
        return
    
    queue = [(root)]

    while queue:
        node = queue.pop(0)

        if node.isTreasure:
            return node.val
        
        if node.left:
            queue.append((node.left))

        if node.right:
            queue.append((node.right))

    return "No treasure in this tree"


result = bfs(root)

root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)

result1 = bfs(root1)

print(result)
print(result1)