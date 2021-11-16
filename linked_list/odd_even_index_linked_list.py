# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]: 
        """
        what happens for
        1. zero element(done) if condition
        2. one element(done) while wont run
        3. two elements(done) while wont run
        4. three(odd) elements(done) while run once, even will be none
        5. four(even) elements(done) while run once, even.next will be none
        """
        # no elements
        if head is None:
            return None
            
        odd, even = head, head.next
        even_head = even
                
        # check next 2 pointers
        while even and even.next: #gain point
            # propagagte odd
            odd.next = even.next
            odd = odd.next
            
            # propagate even
            even.next = odd.next
            even = even.next

        odd.next = even_head
        return head