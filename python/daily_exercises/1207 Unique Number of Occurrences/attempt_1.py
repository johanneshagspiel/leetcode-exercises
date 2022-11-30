class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        count_arr = [0] * 2001

        for num in arr:
            count_arr[num + 1000] += 1

        occ_arr = [0] * 1001

        for occ in count_arr:

            if occ != 0:
                if occ_arr[occ] != 0:
                    return False

                occ_arr[occ] = 1

        return True
