# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseLinkedList(self, head, k):
        """
        We will use while loop, NO need to get start and end pointer
        """
        prev, curr = None, head
        while k: # in place of while curr:
            agla = curr.next
            curr.next = prev
            prev = curr
            curr = agla
            k -= 1
        
        return prev

    # unintutitive could not understand
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        we won't be making use of the stack here and rather use a 
        COUPLE ADDITIONAL VARIABLES to maintain the proper connections along the way
        
        We keep doing this until we reach the end of the list 
        or we encounter that there are < k nodes left in the list
        """
        ptr = head
        ktail = None
        
        new_head = None
        while ptr:
            count = 0
            ptr = head
            
            while count < k and ptr:
                ptr = ptr.next
                count += 1
                
            if count == k:
                # rev_head is where the reversed pointer stored
                rev_head = self.reverseLinkedList(head, k)
                
                if not new_head:
                    new_head = rev_head
            
                # THIS IS IMPORTANT, 
                # for the first group
                # ktail is None we don't do anything
                if ktail:
                    ktail.next = rev_head

                ktail = head
                head = ptr
                # ALL propagation done when count == k
        
        # for nodes having length < k
        # attach the final, possibly un-reversed portion
        if ktail:
            ktail.next = head
                
        return new_head if new_head else head