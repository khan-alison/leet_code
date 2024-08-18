# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ptr1 = l1
        ptr2 = l2

        carry = 0
        res_head = ListNode()
        res_ptr = res_head
        while prt1 or prt2:
            val1 = prt1.val if prt1 else 0
            val2 = prt2.val if prt2 else 0
            add = val1 + val2 + carry
            remainder = add % 10
            carry = add // 10
            new_res_node = ListNode(remainder)
            res_ptr.next = new_res_node
            res_ptr = res_ptr.next

            ptr1 = ptr1.next if ptr1 else None
            ptr2 = ptr2.next if ptr2 else None
        
        if carry:
            res_ptr
        # def list_to_number(node):
        #     result = 0
        #     multiplier = 1
        #     while node:
        #         result += node.val * multiplier
        #         multiplier *= 10
        #         node = node.next
        #     return result

        # def number_to_list(num):
        #     dummy = ListNode(0)
        #     current = dummy
        #     for digit in str(num)[::-1]:
        #         current.next = ListNode(int(digit))
        #         current = current.next
        #     return dummy.next

        # result = list_to_number(l1) + list_to_number(l2)
        
        # return number_to_list(result)

l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))

solution = Solution()
result = solution.addTwoNumbers(l1, l2)
# print(result)
print(10%10)
print(10 // 10)