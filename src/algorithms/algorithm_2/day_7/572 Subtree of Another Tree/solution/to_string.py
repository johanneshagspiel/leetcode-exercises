class Solution(object):
    def isSubtree(self, root, subRoot):

        def tree_to_str(root):
            if root:
                return f"#{root.val} {tree_to_str(root.left)} {tree_to_str(root.right)}"
            return None

        if not root:
            return False
        elif not subRoot:
            return True
        else:

            root_str = tree_to_str(root)
            subRoot = tree_to_str(subRoot)

            return subRoot in root_str