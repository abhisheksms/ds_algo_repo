# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        First we will add an auxiliary "dummy" node, which points to the 
        list head. The "dummy" node is used to simplify some corner cases 
        such as a list with only one node, or removing the head of the 
        list
        
        We maintain a gap of n between first and second
        """
        dummy = ListNode()
        dummy.next = head
        
        first = second = dummy
        for _ in range(n):
            # if n is larger
            if second is None:
                dummy.next = dummy.next.next
                return dummy.next
            second = second.next
            
        # we could have gone just with second.next
        # but we went with while second to handle edge case
        # of single node
        while second and second.next:
            second = second.next
            first = first.next
            
        # no need fro prev
        first.next = first.next.next
        
        return dummy.next


# Without dummy pointer
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = second = head
        for _ in range(n):
            second = second.next
            
        if second is None:
            return head.next
            
        while second and second.next:
            second = second.next
            first = first.next
            
        first.next = first.next.next
        return head