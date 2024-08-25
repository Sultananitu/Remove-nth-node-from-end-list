# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return head
        
        total = 0
        node = head
        while node:
            total += 1
            node = node.next
            
        if total == n:
            return head
        
        count = total - n
        node = head
        while node:
            count -= 1
            if count == 0:
                next_node = node.next
                node.next = next_node.next
                return head
            node = node.next
            
        return None
        
        
        