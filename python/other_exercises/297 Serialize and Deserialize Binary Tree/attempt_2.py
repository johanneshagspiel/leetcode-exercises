# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        data = ""

        stack = []
        stack.append(root)

        while stack:

            node = stack.pop()

            if node:
                data += str(node.val) + ","

                stack.append(node.right)
                stack.append(node.left)

            else:
                data += "n,"

        return data



    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        node_list = data.split(",")

        def rec_deserialize(node_list):
            if node_list[0] == "n":
                node_list.pop(0)
                return None

            root = TreeNode(int(node_list.pop(0)))
            root.left = rec_deserialize(node_list)
            root.right = rec_deserialize(node_list)
            return root

        root = rec_deserialize(node_list)
        return root
