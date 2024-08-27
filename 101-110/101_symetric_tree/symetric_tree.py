# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSymmetric(self, root):
        flag = True
        root1 = root
        root2 = root
        while root1 or root2:
            if root1 and root2:
                if(root1.val == root2.val):
                    root1 = root1.left
                    root2 = root2.right
                else:
                    return False
            else:
                return False
                
        roots = Solution.inorderTraversal(self, root)
        print(roots)
        while roots:
            if(len(roots) == 1):
                return True
            if roots[0] == roots[- 1]:
                roots.pop(0)
                roots.pop(-1)
            else:
                return False


    def inorderTraversal(self, root):
        roots = []
        if root:
            roots.append(root.val)

            if (root and (root.left or root.right)):
                if (root.left):
                    n1 = Solution.inorderTraversal(self, root.left)
                    count = 0
                    while count < len(n1):
                        roots.insert(0, n1[len(n1) - count - 1])
                        count += 1

                if (root.right):
                    n2 = Solution.inorderTraversal(self, root.right)
                    count = 0
                    while count < len(n2):
                        roots.append(n2[count])
                        count += 1


        return roots