from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root == None:
            return None
        else:

            if root.left == None and root.right == None:
                return None
            elif root.left != None:
                self.flatten(root.left)
                tmp_right = root.right
                root.right = root.left
                root.left = None

                itr = root.right
                while itr.right != None:
                    itr = itr.right

                itr.right = tmp_right

            self.flatten(root.right)