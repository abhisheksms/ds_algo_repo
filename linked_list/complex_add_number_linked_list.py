# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# global variables
res = None
carry = 0

class Solution:
    def restart_global_var(self):
        global res, carry
        res = None
        carry = 0
        
    def getsize(self, head):
        n = 0
        while head:
            head = head.next 
            n += 1
            
        return n
    
    def add_numbers(self, l1, l2):
        global res, carry
        if l1 and l2:
            self.add_numbers(l1.next, l2.next)
            total = l1.val + l2.val + carry
            node = ListNode(total%10)
            carry = total // 10
            if res:
                node.next = res
            
            res = node
            
    def add_remaining(self, head, tail):  # pain point 1
        global res, carry
        if head != tail:
            self.add_remaining(head.next, tail)
            val = head.val + carry
            node = ListNode(val % 10)
            node.next = res
            res = node
            carry = val // 10
            
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        self.restart_global_var()
        if l1 is None:
            return l2
        
        if l2 is None:
            return l1
        
        nl1 = self.getsize(l1)
        nl2 = self.getsize(l2)
        
        # if size equal
        if nl1 == nl2:
            self.add_numbers(l1, l2)
        
        else:
            diff = abs(nl1 - nl2) # pain point 2 
            
            if nl1 > nl2:
                start = l1
                for _ in range(diff):
                    l1 = l1.next
                    
                # conventionally add common place numbers
                self.add_numbers(l1, l2)    # pain point 3
                self.add_remaining(start, l1)
                
            else:
                start = l2
                for _ in range(diff):
                    l2 = l2.next
                    
                # conventionally add common place numbers
                self.add_numbers(l1, l2)
                
                # now add remaining numbers and 1
                self.add_remaining(start, l2)
        
        
        global res, carry  
        if carry > 0:        # pain point 4
            node = ListNode(carry)
            node.next = res
            res = node
                
        return res