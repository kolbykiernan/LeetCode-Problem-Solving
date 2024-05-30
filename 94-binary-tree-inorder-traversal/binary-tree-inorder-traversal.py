# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
         
        def traverse(node):
            if node:
                traverse(node.left)
                stack.append(node.val)
                traverse(node.right)
        
        traverse(root)
        return stack











        # root_node = root[0] 
        # next_node += root_node
        # for char in range(root)
        #     if val.next_node != val.root_node + 1:
        #         stack.append[root_node]
        #         root_node ++
        #         next_node ++


        #     else:
             




        # if the next number in root is 2, 
        #     then 1 has a left child, 
        # else
        #     we will go back to the root
        #     then "visit" record the node
        # then we go to the right child,
        # if the next number in root is 3,
        #     then 2 has a left child
        #     then we check if three has a left child
        #     if it doesnt, visit 3 and move to the right child
        #     see if the right child has children
        #     if not, we visit 2, then check if 2 has a right child
        #      if it doenst the binary tree traversal is complete
        



        