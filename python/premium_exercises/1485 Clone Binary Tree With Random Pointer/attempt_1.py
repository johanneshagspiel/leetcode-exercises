# Definition for Node.
class Node:
    def __init__(self, val=0, left=None, right=None, random=None):
        self.val = val
        self.left = left
        self.right = right
        self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':

        index_dic = {}

        final_index_dic, first_root_copy = self.first_iteration(root, index_dic)
        second_root_copy, root, input_index_dic = self.second_iteration(first_root_copy, root, final_index_dic)

        return second_root_copy

    def first_iteration(self, root, input_index_dic):

        if not root:
            return input_index_dic, root
        else:
            root_copy = NodeCopy()
            root_copy.val = root.val

            left_index_dic, root_copy.left = self.first_iteration(root.left, input_index_dic)
            final_index_dic, root_copy.right = self.first_iteration(root.right, left_index_dic)

            new_key = hash(root)
            final_index_dic[new_key] = root_copy

            return final_index_dic, root_copy

    def second_iteration(self, root_copy, original_root, input_index_dic):

        if not original_root or not root_copy:
            return root_copy, original_root, input_index_dic

        else:
            original_random = original_root.random

            if original_random:
                original_random_hash = hash(original_random)
                found_random = input_index_dic[original_random_hash]
                root_copy.random = found_random

            self.second_iteration(root_copy.left, original_root.left, input_index_dic)
            self.second_iteration(root_copy.right, original_root.right, input_index_dic)

            return root_copy, original_root, input_index_dic