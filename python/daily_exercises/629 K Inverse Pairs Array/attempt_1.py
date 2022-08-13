class Solution:
    def kInversePairs(self, n: int, k: int) -> int:

        def determine_is_possible(num, sum):

            if sum == k:
                return True

            elif sum > k:
                return False

            elif num > n:
                return False

            else:
                num += 1
                sum += (num - 1)
                return determine_is_possible(num, sum)


        def calculate_determine_section(num, sum):

            if sum == k:
                return num
            else:
                num += 1
                sum += (num - 1)
                return calculate_determine_section(num, sum)

        if k == 0:
            return 1

        is_possible = determine_is_possible(2, 1)
        if not is_possible:
            return 0
        else:
            determined_section = calculate_determine_section(2, 1)
            free_section = n - determined_section

