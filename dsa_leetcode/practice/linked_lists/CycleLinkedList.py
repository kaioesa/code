# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head 
        fast = head
        
        # Same strategy as the middle of the linked list.
        # We have a fast and slow pointer, each move in a fixed way, but different frequencies.
        # For this cycle thing, we just have to compare the current values.
        while fast and fast.next:
            slow = slow.next  
            fast = fast.next.next
            
            if slow == fast:
                return True
        return False