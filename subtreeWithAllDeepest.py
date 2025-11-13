# Definition for a binary tree node.
from typing import Optional, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        _, ans = self.dfs(root, 0)
        return ans

    def dfs(
        self, root: Optional[TreeNode], depth: int
    ) -> Tuple[int, Optional[TreeNode]]:
        if root is None:
            return depth, None
        leftDepth, leftLCA = self.dfs(root.left, depth + 1)
        rightDepth, rightLCA = self.dfs(root.right, depth + 1)
        if leftDepth > rightDepth:
            return leftDepth, leftLCA
        if rightDepth > leftDepth:
            return rightDepth, rightLCA
        return leftDepth, root

sln = Solution()
# root = [3,5,1,6,2,0,8,null,null,7,4]
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

sln.subtreeWithAllDeepest(root)