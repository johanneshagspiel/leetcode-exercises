# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        stack = []
        stack.append((root, root.left, 0, None, None))
        stack.append((root, root.right, 0, None, None))

        start_node_dic = {}

        while stack:
            prev_node, current_node, length, mode, start_node = stack.pop()

            if current_node:
                if not mode:
                    if current_node.val == (prev_node.val + 1):
                        stack.append((current_node, current_node.left, length + 1, "inc", start_node))
                        stack.append((current_node, current_node.right, length + 1, "inc", start_node))

                        if start_node not in start_node_dic:
                            start_node_dic[start_node] = {}
                        if "inc" not in start_node_dic[start_node]:
                            start_node_dic[start_node]["inc"] = 0

                    elif current_node.val == (prev_node.val - 1):
                        stack.append((current_node, current_node.left, length + 1, "dec", start_node))
                        stack.append((current_node, current_node.right, length + 1, "dec", start_node))

                        if start_node not in start_node_dic:
                            start_node_dic[start_node] = {}
                        if "dec" not in start_node_dic[start_node]:
                            start_node_dic[start_node]["dec"] = 0

                    else:
                        stack.append((current_node, current_node.left, 0, None, None))
                        stack.append((current_node, current_node.right, 0, None, None))


                else:
                    if mode == "inc":
                        if current_node.val == (prev_node.val + 1):
                            stack.append((current_node, current_node.left, length + 1, "inc", start_node))
                            stack.append((current_node, current_node.right, length + 1, "inc", start_node))

                        else:
                            prev_len = start_node_dic[start_node]["inc"]
                            start_node_dic[start_node]["inc"] = max(prev_len, length)

                            stack.append((current_node, current_node.left, 0, None, None))
                            stack.append((current_node, current_node.right, 0, None, None))

                    elif mode == "dec":
                        if current_node.val == (prev_node.val - 1):
                            stack.append((current_node, current_node.left, length + 1, "dec", start_node))
                            stack.append((current_node, current_node.right, length + 1, "dec", start_node))

                        else:
                            prev_len = start_node_dic[start_node]["dec"]
                            start_node_dic[start_node]["dec"] = max(prev_len, length)

                            stack.append((current_node, current_node.left, 0, None, None))
                            stack.append((current_node, current_node.right, 0, None, None))
            else:
                if mode:
                    if mode == "inc":
                        prev_len = start_node_dic[start_node]["inc"]
                        start_node_dic[start_node]["inc"] = max(prev_len, length)
                    elif mode == "dec":
                        prev_len = start_node_dic[start_node]["dec"]
                        start_node_dic[start_node]["dec"] = max(prev_len, length)


        max_path_len = 1

        for start_node, mode_dic in start_node_dic.items():
            cur_path_len = 1
            for path_len in mode_dic.values():
                cur_path_len += path_len
            max_path_len = max(max_path_len, cur_path_len)

        return max_path_len
