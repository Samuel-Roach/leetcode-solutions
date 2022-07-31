from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def getIntFromLinked(node):
            temp = node
            value = 0
            power = 0

            while temp != None:
                value += pow(10, power) * temp.val
                temp = temp.next
                power += 1

            return value

        l1_val = getIntFromLinked(l1)
        l2_val = getIntFromLinked(l2)
        total = l1_val + l2_val
        total_str = str(total)

        original = ListNode(val=int(total_str[-1]))
        current_place = original
        total_str = total_str[:-1]

        while len(total_str) > 0:
            current_place.next = ListNode(val=int(total_str[-1]))
            total_str = total_str[:-1]
            current_place = current_place.next

        return original