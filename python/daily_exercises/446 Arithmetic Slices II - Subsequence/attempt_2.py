class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:

        # nums.sort()
        num_dic = collections.Counter(nums)
        res = 0

        for i in range(len(nums)):

            start_num = nums[i]
            considered_distances = set()

            for j in range(i + 1, len(nums)):
                other_num = nums[j]
                distance = other_num - start_num

                if distance not in considered_distances:
                    considered_distances.add(distance)
                    sec_len = 2

                    decreased = []

                    num_dic[other_num] -= 1
                    decreased.append(other_num)

                    while (other_num + distance in num_dic and num_dic[other_num + distance] > 0):
                        sec_len += 1
                        other_num = other_num + distance
                        num_dic[other_num] -= 1
                        decreased.append(other_num)

                    for num in decreased:
                        num_dic[num] += 1

                    if sec_len >= 3:
                        temp = sec_len - 2
                        res += temp

        return res

