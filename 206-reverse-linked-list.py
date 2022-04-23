# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# iterative
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        return prev


# recursive
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # hit only if head is empty
        if not head:
            return None

        tmp = head

        # reverse the rest of the list
        if head.next:
            tmp = self.reverseList(head.next)
            # put the first element at the end
            head.next.next = head
            # if at end, head.next is already None
            head.next = None

        # fix the head pointer
        return tmp

