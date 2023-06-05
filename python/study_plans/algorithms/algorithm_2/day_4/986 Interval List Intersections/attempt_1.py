from typing import List
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

        pointer_list_1 = 0
        pointer_list_2 = 0

        len_first_list = len(firstList)
        len_second_list = len(secondList)

        output_list = []

        while pointer_list_1 < len_first_list and pointer_list_2 < len_second_list:
            first_element = firstList[pointer_list_1]
            second_element = secondList[pointer_list_2]

            start_list_1 = first_element[0]
            end_list_1 = first_element[1]

            start_list_2 = second_element[0]
            end_list_2 = second_element[1]

            if start_list_1 <= start_list_2 and start_list_2 <= end_list_1:
                start_overlap = start_list_2
                end_overlap = min(end_list_1, end_list_2)
                output_list.append([start_overlap, end_overlap])

                if end_list_1 <= end_list_2:
                    pointer_list_1 += 1
                else:
                    pointer_list_2 += 1

            elif end_list_2 >= start_list_1:
                start_overlap = start_list_1
                end_overlap = end_list_2
                output_list.append([start_overlap, end_overlap])

                if end_list_1 <= end_list_2:
                    pointer_list_1 += 1
                else:
                    pointer_list_2 += 1

            else:
                if end_list_1 <= end_list_2:
                    pointer_list_1 += 1
                else:
                    pointer_list_2 += 1

        return output_list

if __name__ == "__main__":
    solution = Solution()
    solution.intervalIntersection([[10,12],[18,19]], [[1,6],[8,11],[13,17],[19,20]])