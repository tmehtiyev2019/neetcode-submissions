# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        point_1=head
        point_2=head
        # check 

        while point_2 and point_2.next:
            point_1=point_1.next
            point_2=point_2.next.next
            if point_1==point_2:
                return True
        return False
            

        