# Runtime: 100 ms
# Memory Usage: 23.2 MB

# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

# You may not modify the values in the list's nodes, only nodes itself may be changed.

# Given 1->2->3->4, reorder it to 1->4->2->3.
# Given 1->2->3->4->5, reorder it to 1->5->2->4->3.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        if(head == None or head.next == None): return
        
        slow, fast = head, head
        while(fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
        
        prev, curr = None, slow
        while(curr != None):
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        n1, n2 = head, prev
        while(n2.next != None):
            tmp = n1.next
            n1.next = n2
            n1 = tmp
            
            tmp = n2.next
            n2.next = n1
            n2 = tmp
