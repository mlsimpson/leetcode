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

# another recursive solution
def reverseList(head):
    # Base case, returns null on empty list
    # returns the 'last' node on a non-empty list
    if not head or not head.next:
        return head

    rev_list = reverseList(head.next)
    # tricky to think about:
    # head.next's "next" pointer is the current head
    # which reverses the pointer
    head.next.next = head
    # We set head.next to None for two reasons:
    # 1 - The final list needs to end in "None"
    # 2 - each "previous" recursive call (lower on the call stack)
    #     will override None as the call stack pops
    head.next = None

    return rev_list

