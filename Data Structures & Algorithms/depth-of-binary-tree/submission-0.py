# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Here we can use the BFS method 
        if not root: 
            return 0
        
        deque = collections.deque()
        deque.append(root)
        count = 0

        while deque: 
            count += 1
            for i in range(len(deque)): 
                node = deque.popleft()
                if node: 
                    if node.left: 
                        deque.append(node.left)
                    
                    if node.right: 
                        deque.append(node.right)
        return count 