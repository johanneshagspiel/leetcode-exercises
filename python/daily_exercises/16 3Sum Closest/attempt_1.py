import collections


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        n = len(nums)

        two_sums = []
        min_num = -float("inf")
        max_num = float("inf")

        num_dic = collections.defaultdict(set)

        for i in range(n):
            num_1 = nums[i]
            min_num = min(min_num, num_1)
            max_num = max(num_1, max_num)
            num_dic[num_1].add(i)

            for j in range(i + 1, n):
                num_2 = nums[j]
                index_set = set()
                index_set.add(i)
                index_set.add(j)
                two_sums.append((target - num_1 - num_2, index_set))


        res = float("inf")

        for missing_num, index_set in two_sums:

            if missing_num in num_dic:
                found_set = num_dic[missing_num]
                dif = found_set - index_set
                if len(dif) > 0:
                    return 0

            
