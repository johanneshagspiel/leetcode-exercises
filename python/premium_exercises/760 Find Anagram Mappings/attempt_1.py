class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:

        nums2_index_dic = {}

        for index, num in enumerate(nums2):
            if num not in nums2_index_dic:
                nums2_index_dic[num] = []
            nums2_index_dic[num].append(index)

        res = []
        for num1 in nums1:
            res_index = nums2_index_dic[num1].pop()
            res.append(res_index)

        return res
