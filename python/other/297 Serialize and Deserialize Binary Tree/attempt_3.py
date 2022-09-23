# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections


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
        def rec_deserialization(node_queue):

            if node_queue[0] == 'n':
                node_queue.popleft()
                return None

            else:
                root = TreeNode(int(node_queue.popleft()))
                root.left = rec_deserialization(node_queue)
                root.right = rec_deserialization(node_queue)

                return root


        node_queue = collections.deque(data.split(","))
        root = rec_deserialization(node_queue)
        return root
