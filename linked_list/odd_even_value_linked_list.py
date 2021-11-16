class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # is is similar to head and tail
        even_start = ListNode(-22)
        odd_start = ListNode(-11)
        even = even_start
        odd = odd_start
        
        while head:
            if head.val % 2 == 0:
                even.next = head
                even = even.next
            else:
                odd.next = head
                odd = odd.next
                
            head = head.next
        
        odd.next = even_start.next
        even.next = None # missed
        return odd_start.next