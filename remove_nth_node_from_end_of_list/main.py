# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode()
        dummy.next = head

        left = right = dummy
        for i in range(n):
            right = right.next

        while right.next:
            right = right.next
            left = left.next
          
        left.next = left.next.next
        return dummy.next

        # length = 0
        # result = []
        # while head:
        #     result.append(head.val)
        #     head = head.next
        #     length += 1
        # result.pop(-n)

        # res_head = ListNode()
        # res_ptr = res_head
        # for value in result:
        #     res_ptr.next = ListNode(value)
        #     res_ptr = res_ptr.next

        # return res_head.next


l = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
n = 2
solution = Solution()
result = solution.removeNthFromEnd(l, n)
while result.next:
  print(result.val)
  result = result.next
