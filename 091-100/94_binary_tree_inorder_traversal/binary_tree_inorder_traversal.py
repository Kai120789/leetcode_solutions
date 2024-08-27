# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root):
        roots = []
        if root:
            roots.append(root.val)

            if (root and (root.left or root.right)):
                if (root.left):
                    n1 = Solution.inorderTraversal(Solution.inorderTraversal, root.left)
                    count = 0
                    while count < len(n1):
                        roots.insert(0, n1[len(n1) - count - 1])
                        count += 1

                if (root.right):
                    n2 = Solution.inorderTraversal(Solution.inorderTraversal, root.right)
                    count = 0
                    while count < len(n2):
                        roots.append(n2[count])
                        count += 1


        return roots