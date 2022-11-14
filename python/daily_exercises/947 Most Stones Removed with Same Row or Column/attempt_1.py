class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:

        row_dic = {}
        column_dic = {}
        group_dic = {}
        group_index = 0

        for row, column in stones:

            row_index = -1
            if row in row_dic:
                row_index = row_dic[row]

            column_index = -1
            if column in column_dic:
                column_index = column_dic[column]

            if column_index == -1 and row_index == -1:
                row_dic[row] = group_index
                column_dic[column] = group_index
                group_dic[group_index] = 1
                group_index += 1

            elif column_index == -1 and row_index != -1:
                row_dic[row] = row_index
                column_dic[column] = row_index
                group_dic[row_index] += 1

            elif column_index != -1 and row_index == -1:
                row_dic[row] = column_index
                column_dic[column] = column_index
                group_dic[column_index] += 1

            else:
                if column_index == row_index:
                    row_dic[row] = column_index
                    column_dic[column] = column_index
                    group_dic[column_index] += 1

                else:
                    other_row_dic = row_dic
                    for other_row, other_row_index in other_row_dic.items():
                        if other_row_index == row_index:
                            row_dic[other_row] = column_index

                    other_column_dic = column_dic
                    for other_column, other_column_index in other_column_dic.items():
                        if other_column_index == row_index:
                            column_dic[other_column] = column_index

                    group_dic[column_index] += group_dic[row_index]
                    group_dic.pop(row_index)

        can_be_removed = 0

        for value in group_dic.values():
            if value > 1:
                can_be_removed += value - 1
        return group_dic
