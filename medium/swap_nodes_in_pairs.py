# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        if head.next == None:
            return head
        
        before = ListNode(0, head)
        before_head = before
        while before.next != None and before.next.next != None:
            a = before.next
            b = before.next.next
            after = b.next
            a.next = after
            b.next = a
            before.next = b

            before = before.next.next

        return before_head.next