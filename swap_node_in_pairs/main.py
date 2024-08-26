# https://leetcode.com/problems/swap-nodes-in-pairs/
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode()
        dummy.next = head
        current = dummy

        while current.next and current.next.next:
            first = current.next
            second = current.next.next
            
            first.next = second.next
            second.next = first
            current.next = second

            current = first
        return dummy.next


head = [1, 2, 3, 4]


def createLinkedList(l):
    head = ListNode()
    res_ptr = head
    for i in l:
        res_ptr.next = ListNode(i)
        res_ptr = res_ptr.next
    return head.next


l = createLinkedList(head)
solution = Solution()
result = solution.swapPairs(l)

while result:
    print(result.val)
    result = result.next
