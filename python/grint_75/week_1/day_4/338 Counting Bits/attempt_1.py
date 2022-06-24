from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        answer_list = []

        for number in range(0, n + 1):
            hamming_weight = self.hamming_weight(number)
            answer_list.append(hamming_weight)

        return answer_list

    def hamming_weight(self, n):

        sum = 0
        while n != 0:
            n &= (n - 1)
            sum += 1

        return sum


if __name__ == '__main__':
    solution = Solution()
    n = 2
    output = solution.countBits(n)
    print(output)