class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:

        rows = len(mat)
        columns = len(mat[0])

        keep_going = True
        pointer_list = [(row, 0) for row in range(rows)]

        while keep_going:
            value_list = [mat[row][column] for (row, column) in pointer_list]
            max_element = max(value_list)
            min_element = min(value_list)

            if max_element == min_element:
                return min_element
            else:
                max_column = 0
                unchanged = 0
                index = 0

                for row, column in pointer_list:

                    if column == (columns - 1):
                        max_column += 1
                    else:
                        value = mat[row][column]
                        if value == min_element:

                            new_column = column
                            while (mat[row][new_column] < max_element and new_column < (columns - 1)):
                                new_column += 1

                            pointer_list[index] = (row, new_column)

                        else:
                            unchanged += 1
                    index += 1

                if max_column + unchanged == columns:
                    keep_going = False

        return -1
