# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        ahead = head # got current head
        while ahead and ahead.next: # if ahead have an possible next position
            ahead = ahead.next.next # move ahead twice, if face none, break the loop
            head = head.next # head will step half the speed of ahead, so ahead = 10, head = 5
        return head # return the middle node