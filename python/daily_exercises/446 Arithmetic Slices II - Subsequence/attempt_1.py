class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:

        prev_num = nums[0]
        prev_distance = float("inf")

        prev_len = 1
        art_seq = []

        for i in range(1, len(nums)):
            cur_num = nums[i]

            if i == 1:
                prev_distance = cur_num - nums[0]
                prev_num = cur_num
                prev_len += 1
            else:
                cur_distance = cur_num - prev_num

                if cur_distance == prev_distance:
                    prev_len += 1
                    prev_num = cur_num
                else:
                    if prev_len >= 3:
                        art_seq.append(prev_len)

                    cur_distance = cur_num - prev_num
                    prev_num = cur_num
                    prev_len = 2

        if prev_len >= 3:
            art_seq.append(prev_len)

        res = 0
        for art_subsec in art_seq:
            for possible_length in range(len(art_subsec), 2):
                posibilities = len(art_subsec) -

        return art_seq
