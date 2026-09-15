# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        n1, n2 = head, head.next

        while n1 and n2 and n1.next and n2.next:
            n1 = n1.next
            n2 = n2.next.next

            if n1 == n2:
                return True
        
        return False
        