import collections


class Solution(object):
    def shareCandies(self, candies, k):
        """
        :type candies: List[int]
        :type k: int
        :rtype: int
        """

        my_candies = collections.defaultdict(int)
        max_count = 0

        for candy in candies:
            my_candies[candy] += 1

        if k == 0:
            return len(my_candies.keys())

        for i in range(len(candies)):
            sister_candy = candies[i]

            my_candy_count = my_candies[sister_candy]
            if my_candy_count == 1:
                my_candies.pop(sister_candy)
            else:
                my_candies[sister_candy] -= 1

            if i >= k - 1:
                max_count = max(len(my_candies.keys()), max_count)
                to_add_candy = candies[i-k+1]
                my_candies[to_add_candy] += 1

        return max_count
