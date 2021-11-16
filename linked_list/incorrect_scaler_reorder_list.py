# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
    def find_middle(self, head):
        if head is None:
            return None
        
        # BOTH START FROM THE SAME POINT
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow

    def reverse(self, head):
        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev

    def merge(self, head, end):
        res = ListNode(0)
        start_res = res

        while head and end:
            res.next = head
            res.next.next = end
            res = res.next.next
            head, end = head.next, end.next

        res.next = head if end is None else end

        return start_res.next


	def reorderList(self, A):

        if A is None:
            return None

        mid = self.find_middle(A)

        # the element before mid should point to null
        ptr = A
        while ptr.next != mid:
            ptr = ptr.next 
        ptr.next = None

        end = self.reverse(mid)
        res = self.merge(A, end)
        return res

        