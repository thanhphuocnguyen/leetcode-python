# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        if head == None or head.next == None:
            return True
        slow, fast = head, head
        firstHalf = []
        while fast != None and fast.next != None:
            firstHalf.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        i = len(firstHalf) - 1
        if len(firstHalf) % 2 != 0:
            i -= 1
        while slow != None:
            if slow.val != firstHalf[i]:
                return False
            i -= 1
            slow = slow.next
        return True


sln = Solution()
sln.isPalindrome(ListNode(1, ListNode(0, ListNode(1, ListNode(1)))))
