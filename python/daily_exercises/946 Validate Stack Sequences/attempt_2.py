class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:

        stack = []
        pop_index = 0

        for char in pushed:
            stack.append(char)

            while len(stack) > 0 and pop_index < len(popped) and stack[-1] == popped[pop_index]:
                stack.pop()
                pop_index += 1

        return pop_index == len(popped)
