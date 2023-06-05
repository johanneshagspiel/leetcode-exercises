from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        majority_candidate = None
        majority_vote = 0

        for number in nums:
            if majority_vote == 0:
                majority_candidate = number
            majority_vote += (1 if number == majority_candidate else -1)

        return majority_candidate

if __name__ == "__main__":
    solution = Solution()

    input = [2,2,1,1,1,2,2]
    output = solution.majorityElement(input)
    print(output)
