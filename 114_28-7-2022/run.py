from solution import Solution, TreeNode

s = Solution()

def breadthFirstString(root=None):
    queue = []
    output_values = []

    if root.val == None:
        return f'[]'

    queue.append(root)
    while len(queue) > 0:
        current = queue[0]
        queue = queue[1:]
        if current:
            output_values.append(str(current.val))
            if current.left != None or current.right != None:
                queue.append(current.left)
                queue.append(current.right)
        else:
            output_values.append('null')

    return f'[{",".join(output_values)}]'

# Example 1
root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, None, TreeNode(6)))
print(breadthFirstString(root))

s.flatten(root)
print(breadthFirstString(root))

# Example 2
root = TreeNode(None)
print(breadthFirstString(root))

s.flatten(root)
print(breadthFirstString(root))

# Example 3
root = TreeNode(0)
print(breadthFirstString(root))

s.flatten(root)
print(breadthFirstString(root))