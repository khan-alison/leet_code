# https://leetcode.com/problems/merge-k-sorted-lists/description/
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            rs_list = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                rs_list.append(self.mergeList(l1, l2))

            lists = rs_list
        return lists[0]

    def mergeList(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next


list1 = [1, 4, 5]
list2 = [1, 3, 4]
list3 = [2, 6]


def createLinkedList(l):
    head = ListNode()
    res_ptr = head
    for i in l:
        res_ptr.next = ListNode(i)
        res_ptr = res_ptr.next
    return head.next


l1 = createLinkedList(list1)
l2 = createLinkedList(list2)
l3 = createLinkedList(list3)
lists = [[l1, l2, l3]]

solution = Solution()
result = solution.mergeKLists(lists)
print(result)