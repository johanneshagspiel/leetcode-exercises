class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        max_candies = max(candies)
        res = []

        for candy in candies:
            pot_candy = candy + extraCandies

            if pot_candy >= max_candies:
                res.append(True)
            else:
                res.append(False)

        return res
