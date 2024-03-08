from collections import deque
from typing import List
from math import  inf

class TreeNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):

        if value < self.value:

            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)

        else:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)
    #  Inorder traversal
    # 1. Traverse the left subtree, i.e., call Inorder(left->subtree)
    # 2. Visit the root.
    # 3. Traverse the right subtree, i.e., call Inorder(right->subtree)
    def inorder_traversal(self):  # left
        if self.left:
            self.left.inorder_traversal()
        print(self.value)
        if self.right:
            self.right.inorder_traversal()

    # Preorder traversal
    # 1. Visit the root.
    # 2. Traverse the left subtree, i.e., call Inorder(left->subtree)
    # 3. Traverse the right subtree, i.e., call Inorder(right->subtree)
    def preorder_traversal(self):  # left
        print(self.value)
        if self.left:
            self.left.preorder_traversal()
        if self.right:
            self.right.preorder_traversal()


    # Postorder traversal
    # Preorder traversal
    # 1. Traverse the left subtree, i.e., call Inorder(left->subtree)
    # 2. Traverse the right subtree, i.e., call Inorder(right->subtree)
    # 3. Visit the root.
    def postorder_traversal(self):  # left
        if self.left:
            self.left.postorder_traversal()
        if self.right:
            self.right.postorder_traversal()
        print(self.value)


    def find(self, value):
        if value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.find(value)
        elif value > self.value:
            if self.right is None:
                return False
            else:
                return self.right.find(value)
        else:
            return True

    def maxDepth_recursion(self, tree) -> int: # recursion
        if not tree:
            return 0
        return 1 + max(self.maxDepth_recursion(tree.left), self.maxDepth_recursion(tree.right))

    def maxDepth_BFS(self, tree) -> int: # recursion
        if not tree:
            return 0

        level = 0
        q = deque([tree])

        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            level += 1

        return level


    def maxDepth_DFS(self, tree):

        if not tree:
            return 0

        stack = [[tree, 1]]
        res = 0

        while stack:
            node, depth = stack.pop()

            if node:
                res = max(depth, res)
                stack.append([node.left, depth+1])
                stack.append([node.right, depth+1])

        return res

    def minDepth_recursion(self, tree) -> int: # recursion
        if not tree:
            return 0
        q = deque([tree])
        level = 0

        while q:
            level += 1
            for _ in range(len(q)):
                node = q.popleft()
                if not node.left and not node.right:
                    return level
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)


    def mergeTrees(self, root1, root2):
        if not root1:
            return root2
        if not root2:
            return root1
        # merge the nodes that are overlapped
        root1.value += root2.value
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)

        return root1

    def sortedArrayToBST(self, nums: List[int]):
        if not nums:
            return None

        mid = len(nums)//2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])

        return root

    def hasPathSum(self, tree, targetSum: int) -> int: # recursion
        if not tree:
            return False

        if not tree.left and not tree.right:
            return targetSum == tree.val

        stack = [[tree, tree.value]]



        while stack:
            node, sum_node = stack.pop()


            if not node.left and not node.right and sum_node == targetSum:
                return True
            if node:
                if node.left:
                    stack.append([node.left, sum_node + node.left.value])
                if node.right:
                    stack.append([node.right, sum_node + node.right.value])
        return False



    def levelOrder(self, root):

        if not root:
            return []


        q = deque([root])

        res = [[root.value]]

        while q:
            ar = []
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                    ar.append(node.left.value)
                if node.right:
                    q.append(node.right)
                    ar.append(node.right.value)
            if ar:
                res.append(ar)
        return res


    def zigzagLevelOrder(self, root):

        if not root:
            return []

        level = 1
        q = deque([root])
        res = [[root.value]]

        while q:
            ar = []

            for _ in range(len(q)):

                if level % 2 == 1:
                    node = q.popleft()
                    if node.right:
                        q.append(node.right)
                        ar.append(node.right.value)
                    if node.left:
                        q.append(node.left)
                        ar.append(node.left.value)

                else:
                    node = q.pop()
                    if node.left:
                        q.appendleft(node.left)
                        ar.append(node.left.value)
                    if node.right:
                        q.appendleft(node.right)
                        ar.append(node.right.value)

            if ar:
                res.append(ar)
            level += 1
        return res


    def isValidBAT(self, root):



        def valid(node, left, right):
            if not node:
                return True
            if not left < node.value < right:
                return False

            return valid(node.left, left, node.val) and valid(node.right, node.val, right)

        return valid(root, -inf, inf)






# tree = TreeNode(3)
# for i in [1, 4, 3, 5, 99, 9, 2]:
#     tree.insert(i)

tree1 = TreeNode(10)
for i in [2, 3, 5,  11, 12, 1, 13]:
    tree1.insert(i)

# tree2 = TreeNode(2)
# # tree1.inorder_traversal()
#
# for i in [1, 4]:
#     tree2.insert(i)
# res = tree1.mergeTrees(tree1, tree2)
# print(res.preorder_traversal())

# print(tree1.hasPathSum(tree1, 13))

# print(tree1.levelOrder(tree1))
print(tree1.zigzagLevelOrder(tree1))

