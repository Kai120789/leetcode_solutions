# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p, q) -> bool:
        if p == None and q == None:
            return True

        if (p and q) and (p.val == q.val):
            flag = Solution.isSameTree(self, p.left, q.left)
            if flag:
                flag = Solution.isSameTree(self, p.right, q.right)
        else:
            flag = False

        return flag        