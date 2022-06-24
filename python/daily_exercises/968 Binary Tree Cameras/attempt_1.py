from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        else:
            number_cameras = math.inf

            stack_1 = []
            stack_1.append((root, 2))
            camera_result_1 = self.dfs(stack_1)
            number_cameras = min(camera_result_1, number_cameras)

            stack_2 = []
            stack_2.append((root, 1))
            stack_2.append((root.left, 2))
            stack_2.append((root.right, 0))
            camera_result_2 = self.dfs(stack_2)
            number_cameras = min(camera_result_2, number_cameras)

            stack_3 = []
            stack_3.append((root, 1))
            stack_3.append((root.left, 0))
            stack_3.append((root.right, 2))
            camera_result_3 = self.dfs(stack_3)
            number_cameras = min(camera_result_3, number_cameras)

            return number_cameras


    def dfs(self, stack, start_number_cameras):

        number_cameras = 0
        number_cameras += start_number_cameras

        while stack:
            current_node, camera_coverage = stack.pop()

            if current_node:

                if camera_coverage > 0:
                    stack.append((current_node.left, camera_coverage - 1))
                    stack.append((current_node.right, camera_coverage - 1))
                else:
                    number_cameras += 1

                    stack.append((current_node.left, 1))
                    stack.append((current_node.right, 1))

        return number_cameras
