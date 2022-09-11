class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1) > len(nums2):
            temp = nums1
            nums1 = nums2
            nums2 = temp

        len_1 = len(nums1)
        len_2 = len(nums2)

        position_1 = 0
        position_2 = 0

        combined_list = []

        while position_1 < len_1 and position_2 < len_2:

            if nums1[position_1] <= nums2[position_2]:
                combined_list.append(nums1[position_1])
                position_1 += 1
            else:
                combined_list.append(nums2[position_2])
                position_2 += 1

        if position_1 < (len_1):
            combined_list.extend(nums1[position_1:len_1])

        if position_2 < (len_2):
            combined_list.extend(nums2[position_2:len_2])

        combined_len = len(combined_list)

        if combined_len % 2 == 0:
            first_element = combined_list[(combined_len // 2) - 1]
            second_element = combined_list[combined_len // 2]

            return (first_element + second_element) / 2

        else:
            return combined_list[combined_len // 2]
