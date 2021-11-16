class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        # BOTH START FROM THE SAME POINT
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow