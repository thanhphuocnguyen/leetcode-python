# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.i = 0

    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        return self.dfs(traversal, 0)

    def dfs(self, traversal: str, depth: int) -> Optional[TreeNode]:
        if self.i > len(traversal):
            return None
        currDepth = 0
        while self.i < len(traversal) and traversal[self.i] == "-":
            currDepth += 1
            self.i += 1
        if currDepth < depth:
            # go back to the previous depth
            self.i -= currDepth
            return None

        x = 0
        while self.i < len(traversal) and traversal[self.i] != "-":
            # convert the string to an integer
            x = x * 10 + int(traversal[self.i])
            self.i += 1
        # create a new node
        node = TreeNode(x)
        # recursively build the left and right subtree
        node.left = self.dfs(traversal, depth + 1)
        node.right = self.dfs(traversal, depth + 1)
        return node
