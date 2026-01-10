# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        new_list = None

        # head = [1,2,3,4,5]
        while head:
            # next node from head, it would be 1
            next_node = head.next 
            # next node saves in new_list. new_list = [1] now
            head.next = new_list
            # new_list now becomes head, so [1]
            new_list = head
            # head moves to next node, which is 2 now, it add to the new_list form the left, so always add in to the beginning, so new_list = [2,1] 
            head = next_node
        
        return new_list
