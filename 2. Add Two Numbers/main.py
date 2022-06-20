from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        solution = self.add_two_nodes(l1, l2)
        return solution

    def add_two_nodes(self, node_1: ListNode, node_2: ListNode, carry=0) -> ListNode:
        total = node_1.val + node_2.val + carry
        val = total % 10
        carry = int(total / 10)
        if node_1.next == None and node_2.next == None:
            if carry == 0:
                return ListNode(val=val)
            else:
                return ListNode(val=val, next=ListNode(val=carry))
        elif node_1.next == None:
            return ListNode(val=val, next=self.add_two_nodes(ListNode(val=0), node_2.next, carry))
        elif node_2.next == None:
            return ListNode(val=val, next=self.add_two_nodes(node_1.next, ListNode(val=0), carry))
        else:
            return ListNode(val=val, next=self.add_two_nodes(node_1.next, node_2.next, carry))

def test(l1, l2):
    is_first = True
    for reversed_ite in reversed(range(len(l1))):
        if is_first:
            exec(f"l1_{reversed_ite} = ListNode(val={l1[reversed_ite]})")
            is_first = False
        else:
            exec(f"l1_{reversed_ite} = ListNode(val={l1[reversed_ite]}, next=l1_{reversed_ite+1})")
    is_first = True
    for reversed_ite in reversed(range(len(l2))):
        if is_first:
            exec(f"l2_{reversed_ite} = ListNode(val={l2[reversed_ite]})")
            is_first = False
        else:
            exec(f"l2_{reversed_ite} = ListNode(val={l2[reversed_ite]}, next=l2_{reversed_ite+1})")
    exec("solution = Solution()")
    exec("solution_node = solution.addTwoNumbers(l1_0, l2_0)")

if __name__ == '__main__':
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    test(l1, l2)
    l1 = [0]
    l2 = [0]
    test(l1, l2)
    l1 = [9, 9, 9, 9, 9, 9, 9]
    l2 = [9, 9, 9, 9]
    test(l1, l2)
