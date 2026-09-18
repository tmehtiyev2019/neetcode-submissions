# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:



# handle ed cases:
# 1. both are empty
# 2. Either is empty

# create a new linked list



        curr1 = list1
        curr2 = list2 
        newNode = ListNode()
        currNew = newNode


        if list1 and not list2:
            return list1

        if list2 and not list1:
            return list2

        if not list1 and not list2:
            newNode

        while curr1 and curr2: # Handle the none cases
            if curr1.val>=curr2.val:
                currNew.next = curr2
                curr2 = curr2.next
            else:
                currNew.next = curr1
                curr1 = curr1.next
            currNew = currNew.next

        if curr1:
            currNew.next = curr1
        elif curr2:
            currNew.next = curr2

        return newNode.next





