class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = ""

        stack = []
        stack.append(root)

        while stack:

            node = stack.pop()

            if node:
                res += str(node.val) + ","

                stack.append(node.right)
                stack.append(node.left)
            else:
                res += "n,"

        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def rec_deserialize(list):

            if list[0] == "n":
                list.pop(0)
                return None

            root = TreeNode(int(list[0]))
            list.pop(0)
            root.left = rec_deserialize(list)
            root.right = rec_deserialize(list)
            return root

        node_list = data.split(",")
        root = rec_deserialize(node_list)
        return root
