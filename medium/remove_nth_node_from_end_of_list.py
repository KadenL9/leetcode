# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        front = head
        for x in range(n):
            front = front.next

        master = ListNode(0, head)
        curr = head
        while front != None:
            curr = curr.next
            front = front.next
            master = master.next

        if curr == head:
            return head.next
        
        master.next = curr.next
        
        return head