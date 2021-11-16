class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        num = 0

        # or num for the case
        # l1 = [9 9]
        # l2 = [1]
        # leaves a carry of one
        while l1 or l2 or num:
            if l1:
                num += l1.val
                l1 = l1.next
            
            if l2:
                num += l2.val
                l2 = l2.next
                
            tail.next = ListNode(num % 10)
            tail = tail.next
            
            # becomes carry for the next iteration
            num //= 10
            
        
        return dummy.next