# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodeDict = {}
        temp = head
        while temp:
            if nodeDict.get(temp):
                return True
            nodeDict[temp] = True
            temp = temp.next
        return False
