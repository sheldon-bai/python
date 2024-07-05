from collections import deque

class Solution:
    def levelOrder(self, root):
        if root is None:
            return []
        
        queue = deque([root])
        result = []

        while queue:
            level = []

            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level)

        return result
    
    # why use deque, not list
    # Because:
    # queue = [1, 2, 3]

    # queue.pop(0)
    # queue.append(4)

    # The time complexity of queue.pop(0) is O(n), since all value need to shift