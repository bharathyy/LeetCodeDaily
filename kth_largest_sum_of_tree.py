from collections import deque
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1

        level_sums = []  
        
        def bfs(root):
            lst = deque([root])
            
            while lst:
                level_size = len(lst)
                level_sum = 0  
                
                for i in range(level_size):
                    curr = lst.popleft()
                    level_sum += curr.val
                    
                    if curr.left:
                        lst.append(curr.left)
                    if curr.right:
                        lst.append(curr.right)
                
                level_sums.append(level_sum)
        
        bfs(root)
        
        level_sums.sort(reverse=True)
        
        if k <= len(level_sums):
            return level_sums[k-1]  
        else:
            return -1  

