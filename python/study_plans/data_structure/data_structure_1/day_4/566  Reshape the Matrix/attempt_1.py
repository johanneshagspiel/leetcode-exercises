from typing import List

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:

        m = len(mat)
        n = len(mat[0])
        entries_original = m * n
        entries_reshaped = r * c

        if entries_reshaped != entries_original:
            return mat

        new_m = [0]*r

        for row in range(r):
            new_m[row] = [0]*c

        start_r = 0
        start_c = 0

        for row in range(r):
            for column in range(c):
                new_m[row][column] = mat[start_r][start_c]

                if start_c + 1 >= n:
                    start_r += 1
                    start_c = 0
                else:
                    start_c += 1

        return new_m


if __name__ == '__main__':

    solution = Solution()
    mat = [[1,2],[3,4]]
    r = 2
    c = 4
    output = solution.matrixReshape(mat, r, c)
    print(output)