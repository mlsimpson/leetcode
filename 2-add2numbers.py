# Definition for singly-linked list.
def traverse(node, tens, tempsum):
    tempsum = tempsum + (node.val * tens)
    tens *= 10
    if node.next is not None:
        return traverse(node.next, tens, tempsum)
    else:
        return tempsum

def list2nodes(mylist):
    previousnode = None
    head = None
    while len(mylist) > 0:
        currentnode = ListNode(mylist[0])
        if head is None:
            head = currentnode
        if previousnode is not None:
            previousnode.next = currentnode
        previousnode = currentnode
        mylist.pop(0)

    return head

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        #outnodes = []
        outnodes = ListNode()

        tensmult = 1

        l1_value = traverse(l1, tensmult, 0)
        l2_value = traverse(l2, tensmult, 0)

        #print(l1_value, l2_value)

        mysum = l1_value + l2_value

        mysum_list = [int(x) for x in str(mysum)]

        mysum_list_reverse = mysum_list[::-1]

#        for i in mysum_list_reverse:
#            node = ListNode(i)
#            node.next = ListNode(next(iter(mysum_list_reverse)))
#            print(node.val, node.next.val)
#
        node = list2nodes(mysum_list_reverse)
        #while(node.next is not None):
        #    print(node.val)
        return node



node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

node1.next = node2
node2.next = node3

l2node1 = ListNode(4)
l2node2 = ListNode(4)
l2node3 = ListNode(4)

l2node1.next = l2node2
l2node2.next = l2node3

solution = Solution()
solution.addTwoNumbers(node1, l2node1)
