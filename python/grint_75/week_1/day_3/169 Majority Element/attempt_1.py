from typing import List
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        number_counter = Counter(nums)
        max_number = number_counter.most_common(n=1)[0][0]

        return max_number

if __name__ == "__main__":
    solution = Solution()

    input = [2,2,1,1,1,2,2]
    output = solution.majorityElement(input)
    print(output)

