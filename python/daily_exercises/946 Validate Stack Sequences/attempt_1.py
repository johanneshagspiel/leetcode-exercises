class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:

        stack = []

        pop_index = 0
        push_index = 0
        max_pop = len(popped)
        max_pushed = len(pushed)
        top_element = None

        while pop_index < max_pop or push_index < max_pushed:

            if len(stack) > 0:
                top_element = stack[-1]

                if top_element == popped[pop_index]:
                    stack.pop()
                    pop_index += 1
                else:
                    if push_index < max_pushed:
                        stack.append(pushed[push_index])
                        push_index += 1
                    else:
                        return False

            else:
                stack.append(pushed[push_index])
                push_index += 1

        return True
