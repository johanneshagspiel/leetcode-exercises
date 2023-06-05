# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        return Solution.search_with_start_index(n, 0)

    @staticmethod
    def search_with_start_index(n, start_index):

        mid_point_index = int(n / 2) + start_index
        mid_point_boolean = Solution.isBadVersion(mid_point_index)

        if n == 1:
            return n

        else:

            if mid_point_boolean:
                is_one_below_good = Solution.isBadVersion(mid_point_index - 1)

                if is_one_below_good:
                    return mid_point_index

                else:
                    return Solution.search_with_start_index(mid_point_index, start_index)

            else:
                return Solution.search_with_start_index(n, mid_point_index)


    @staticmethod
    def isBadVersion(version):
        return version >= 4



if __name__ == '__main__':
    solution = Solution()

    input_1 = 5
    output_1 = solution.firstBadVersion(input_1)
    expected_1 = 4

    print(1)
    print(output_1)
    print(output_1 == expected_1)
    print(" ")

