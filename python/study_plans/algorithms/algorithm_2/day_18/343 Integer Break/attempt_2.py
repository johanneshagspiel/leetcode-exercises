class Solution:
    def integerBreak(self, n: int) -> int:

        candidates = [x for x in range(1, n + 1)]
        result_list = []
        n = len(candidates)

        def back_tracking(remaining, current_list, start_index):

            if remaining == 0:
                result_list.append(current_list[::])
                return

            elif remaining < 0:
                return

            else:

                for index in range(start_index, n):

                    remaining -= candidates[index]
                    current_list.append(candidates[index])

                    back_tracking(remaining, current_list, index)

                    remaining += candidates[index]
                    current_list.pop()

        back_tracking(n, [], 0)

        product_list = []
        for list in result_list:
            acc = 1
            for number in list:
                acc *= number
            product_list.append(acc)

        return max(product_list)