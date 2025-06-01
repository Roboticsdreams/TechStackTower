class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class AddTwoNumbers:
    """"
    Add Two Numbers [Medium]

    You are given two non-empty linked lists representing two non-negative integers.
    The digits are stored in reverse order, and each of their nodes contains a single digit.
    Add the two numbers and return the sum as a linked list.
    You may assume the two numbers do not contain any leading zero, except the number 0 itself.

    Example 1:
            [2] --> [4] --> [3]
            [5] --> [6] --> [4] (+)
            ----------------------
            [7] --> [0] --> [8]
            ----------------------

    Input: l1 = [2,4,3], l2 = [5,6,4]
    Output: [7,0,8]
    Explanation: 342 + 465 = 807.

    Example 2:
    Input: l1 = [0], l2 = [0]
    Output: [0]

    Example 3:
    Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    Output: [8,9,9,9,0,0,0,1]

    Constraints:
    The number of nodes in each linked list is in the range [1, 100].
    0 <= Node.val <= 9
    It is guaranteed that the list represents a number that does not have leading zeros.
    """

    def addtwonumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        head = curr = ListNode(0)

        while l1 and l2:
            total = l1.val + l2.val + carry
            curr.next = ListNode(total % 10)
            carry = total // 10
            l1 = l1.next
            l2 = l2.next
            curr = curr.next

        while l1:
            total = l1.val + carry
            curr.next = ListNode(total % 10)
            carry = total // 10
            l1 = l1.next
            curr = curr.next

        while l2:
            total = l2.val + carry
            curr.next = ListNode(total % 10)
            carry = total // 10
            l2 = l2.next
            curr = curr.next

        if carry > 0:
            curr.next = ListNode(carry)

        return head.next

    def arraytolink(self, lst):
        cur = dummy = ListNode(0)
        for e in lst:
            cur.next = ListNode(e)
            cur = cur.next
        return dummy.next

    def linktoarray(self, root):
        arr = []
        while root is not None:
            arr.append(root.val)
            root = root.next
        return arr


def addtwonumbers_main():
    p2 = AddTwoNumbers()
    l1 = p2.arraytolink([1, 2, 3])
    l2 = p2.arraytolink([3, 2, 1])
    l3 = p2.addtwonumbers(l1, l2)
    return p2.linktoarray(l3)
