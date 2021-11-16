class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr, prev, agla, count = head, None, None, 0
        
        while count < k and curr is not None:
            agla = curr.next
            curr.next = prev
            prev = curr
            curr = agla
            count += 1
            
        if agla is not None:
            head.next = self.reverseKGroup(agla, k)
            
        return prev