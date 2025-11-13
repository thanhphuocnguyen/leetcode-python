# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        temp = head
        bits = []
        while temp:
            bits.append(temp.val)
            temp = temp.next
        ans = 0
        base1 = 1
        for i in range(len(bits) - 1, -1, -1):
            ans += base1 * bits[i]
            base1 *= 2
        return ans

