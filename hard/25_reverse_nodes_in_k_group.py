# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k <= 1:
            return head
        
        temp = ListNode(0, head)
        curr = temp

        while True:
            check = curr
            for x in range(k):
                if check == None or check.next == None:
                    return temp.next

                check = check.next
            
            nextsection = check.next
            lastsection = curr
            curr = curr.next
            start = curr

            prev = None
            for x in range(k - 1):
                nextnode = curr.next
                curr.next = prev
                prev = curr
                curr = nextnode

            curr.next = prev
            start.next = nextsection
            lastsection.next = curr

            curr = start

        
        return temp.next
