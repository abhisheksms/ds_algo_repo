# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def find_mid(self, head):
        slow = fast = head
        
        # THIS IS WHAT I THOUGHT
        # while fast and fast.next:
        #     slow = slow.next #NOOOO
        #     fast = slow.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow
    
    
    def reverse(self, head):
        """
        # BEFORE
        1 -> 2 -> 3 -> 2 -> 1
        # AFTER
        1 -> 2 -> 3 <- 2 <- 1

        # BEFORE
        1 -> 2 -> 3 -> 3 -> 2 -> 1
        # AFTER
        1 -> 2 -> 3 <- 3 <- 2 <- 1
        """
        prev, curr = None, head
        while curr:
            # store next in a temp pointer
            temp = curr.next
            # important step
            curr.next = prev
            
            # propagate forward
            prev = curr
            curr = temp
        
        return prev
    
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        mid = self.find_mid(head)
        end = self.reverse(mid)
        
        # how to determine even or odd length?
        # i guess it is not needed, since we starting from end
        
        while head and end:
            if head.val != end.val:
                return False
            
            head = head.next
            end = end.next
            
        return True