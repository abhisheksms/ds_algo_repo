# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def find_mid(self, head):
        if head is None:
            return head
        
        slow = fast = head
        # slight modification, fast shouldd always point to last node
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
            
        return slow
    
    def merge(self, l1, l2):
        temp = ListNode()
        res = temp
        
        while l1 and l2:
            if l1.val <= l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            
            temp = temp.next
        
        temp.next = l1 if l1 else l2
        return res.next
    
        
    
    def sortList(self, node: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merge sort approach
        """
        if node is None or node.next is None:
            return node
        
        middle = self.find_mid(node)
        middle_next = middle.next
        
        middle.next = None
        
        first = self.sortList(node)
        second = self.sortList(middle_next)
        
        res = self.merge(first, second)
        
        return res
        