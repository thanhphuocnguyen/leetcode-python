# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preorderIdx = 0
        inorderDict = dict()
        for i in range(len(inorder)):
            inorderDict[inorder[i]] = i
        return self.buildRecursive(preorder, inorder, 0, len(preorder) - 1)

    def buildRecursive(
        self,
        inorderDict: Dict[int, int],
        preorder: List[int],
        inorder: List[int],
        left: int,
        right: int,
    ) -> Optional[TreeNode]:
        if left > right:
            return None
        val = preorder[self.preorderIdx]
        node = TreeNode(val)
