class Solution:
    def integerBreak(self, n: int) -> int:

        candidates = [x for x in range(1, n)]
        self.result_list = []

        def rec(remaining, position, number_list):
            if remaining == 0:
                self.result_list.append(number_list[::])
                return

            elif remaining < 0:
                return

            elif position == len(candidates):
                return

            else:
                number = candidates[position]
                cum_sum = 0

                while cum_sum <= n:
                    cum_sum += number

                    remaining -= cum_sum
                    number_list.append(number)

                    rec(remaining, position + 1, number_list)

                    remaining += number
                    number_list.pop()

        rec(n, [], 0)
        product_list = []

        for list in self.result_list:
            acc = 1
            for number in list:
                acc *= number
            product_list.append(acc)

        return max(product_list)
