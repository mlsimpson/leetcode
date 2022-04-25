# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        left, right = head, head

        for i in range(1, k):
            left = left.next

		# if we set the 'tail' value to kth-left node,
		# as we find the actual tail node,
		# and set 'right' to head,
		# we'll have the kth-right node when we find tail
        tail = left

        while tail.next:
            right = right.next
            tail = tail.next


        left.val, right.val = right.val, left.val

        return head

