class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:

        res = []

        shift_bits = (1 << 7) - 1

        for index in range(len(nums1)):
            nums1[index] = (nums1[index] << 7) + index
            nums2[index] = (nums2[index] << 7) + index

        nums1.sort()
        nums2.sort()

        res = [0 for _ in range(len(nums1))]

        for index in range(len(nums1)):
            original_index = nums1[index] & shift_bits
            other_index = nums2[index] & shift_bits

            res[original_index] = other_index

        return res
