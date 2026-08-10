# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        first = l1.val + l2.val
        startNode = ListNode(first % 10, None)
        carry = first // 10
        currNode = startNode
        l1 = l1.next
        l2 = l2.next
        while l1 != None or l2 != None or carry == 1:
            if l1 == None:
                l1 = ListNode(0, None)
            if l2 == None:
                l2 = ListNode(0, None)
            total = l1.val + l2.val + carry
            newNode = ListNode(total % 10, None)
            carry = total // 10
            currNode.next = newNode
            currNode = newNode
            l1 = l1.next
            l2 = l2.next
        
        return startNode