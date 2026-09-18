# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = 0
        n2 = 0
        curr1 = l1
        curr2 = l2
        newNode = ListNode()
        curr = newNode

        sum1 = 0 + curr1.val * 10**n1
        sum2 = 0 + curr2.val * 10**n2

        while curr1.next:
            n1 += 1
            curr1 = curr1.next
            sum1 += curr1.val * 10**n1

        
        while curr2.next:
            n2 += 1
            curr2 = curr2.next
            sum2 += curr2.val * 10**n2

        total = sum1 + sum2

        # to change total to linked list
        for i in reversed(str(total)):
            curr.next = ListNode(int(i))
            curr = curr.next
        return newNode.next








# questions:
# how to handle the 
    
# Input: l1 = [1,2,3], l2 = [4,5,6]

# Output: [5,7,9]

# Explanation: 321 + 654 = 975.