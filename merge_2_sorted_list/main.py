# https://leetcode.com/problems/merge-two-sorted-lists/
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        result = ListNode()
        res_ptr = result

        l1_ptr = list1
        l2_ptr = list2

        while l1_ptr and l2_ptr:
            if l1_ptr.val <= l2_ptr.val:
                res_ptr.next = l1_ptr
                l1_ptr = l1_ptr.next
            else:
                res_ptr.next = l2_ptr
                l2_ptr = l2_ptr.next
            res_ptr = res_ptr.next
        if l1_ptr:
            res_ptr.next = l1_ptr
        if l2_ptr:
            res_ptr.next = l2_ptr

        return result.next


list1, list2 = [1, 2, 4],   [1, 3, 4]


def createLinkedList(l):
    head = ListNode()
    res_ptr = head
    for i in l:
        res_ptr.next = ListNode(i)
        res_ptr = res_ptr.next
    return head.next


l1 = createLinkedList(list1)
l2 = createLinkedList(list2)

solution = Solution()
result = solution.mergeTwoLists(l1, l2)


def printLinkedList(node):
    while node:
        print(node.val, end=" ")
        node = node.next
    print()


printLinkedList(result)
