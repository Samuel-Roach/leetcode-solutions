from solution import Solution, ListNode

s = Solution()

def printListNodes(node):
    output = ''
    current = node
    while current != None:
        output += f'{current.val} '
        current = current.next
    return output

# Example 1
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
print(printListNodes(s.addTwoNumbers(l1=l1, l2=l2)))

# Example 2
l1 = ListNode(0)
l2 = ListNode(0)
print(printListNodes(s.addTwoNumbers(l1=l1, l2=l2)))

# Example 3
l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
print(printListNodes(s.addTwoNumbers(l1=l1, l2=l2)))
