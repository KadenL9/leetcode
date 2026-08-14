# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        vals = []
        for l in lists:
            while l != None:
                vals.append(l.val)
                l = l.next
        
        vals = sorted(vals)[::-1]

        head = None
        for val in vals:
            head = ListNode(val, head)
        
        return head