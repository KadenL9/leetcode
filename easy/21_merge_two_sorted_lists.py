# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if list1 == None:
            return list2
        if list2 == None:
            return list1
            
        if list1.val <= list2.val:
            head = ListNode(list1.val, None)
            list1 = list1.next
        else:
            head = ListNode(list2.val, None)
            list2 = list2.next

        curr = head
        while list1 or list2:
            if not list1:
                curr.next = ListNode(list2.val, None)
                list2 = list2.next
            elif not list2:
                curr.next = ListNode(list1.val, None)
                list1 = list1.next
            else:
                if list1.val <= list2.val:
                    curr.next = ListNode(list1.val, None)
                    list1 = list1.next
                else:
                    curr.next = ListNode(list2.val, None)
                    list2 = list2.next
            
            curr = curr.next
        
        return head