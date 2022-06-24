from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal_list = []

        for row in range(numRows):
            new_row = []

            for index in range(row + 1):
                if index == 0 or index == (row):
                    new_row.append(1)
                else:
                    left_value = pascal_list[row - 1][index - 1]
                    right_value = pascal_list[row - 1][index]
                    combined_value = left_value + right_value
                    new_row.append(combined_value)

            pascal_list.append(new_row)

        return pascal_list

if __name__ == '__main__':

    solution = Solution()
    numRows = 5
    output = solution.generate(numRows)
    print(output)
