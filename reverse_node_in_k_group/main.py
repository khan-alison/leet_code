# https://leetcode.com/problems/reverse-nodes-in-k-group/
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode(0, head)
        prevGroup = dummy

        while True:
            kth_node = self.getKthNode(prevGroup, k)

            if not kth_node:
                break

            nextGroup = kth_node.next

            prev, curr = kth_node.next, prevGroup.next

            while curr != nextGroup:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
                
            temp = prevGroup.next
            prevGroup.next = kth_node
            prevGroup = temp
        return dummy.next

    def getKthNode(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr


list1 = [1, 2, 3, 4, 5]
list2 = [1, 3, 4]
list3 = [2, 6]


def createLinkedList(l):
    head = ListNode()
    res_ptr = head
    for i in l:
        res_ptr.next = ListNode(i)
        res_ptr = res_ptr.next
    return head.next


l, k = createLinkedList(list1), 3
solution = Solution()
result = solution.reverseKGroup(l, k)

while result:
    print(result.val)
    result = result.next
