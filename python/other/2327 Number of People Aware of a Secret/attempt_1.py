import collections


class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:

        dp = [0 for _ in range(forget)]
        dp[0] = 1

        for day in range(n-1):
            dp.insert(0, 0)
            dp.pop()
            dp[0] = sum(dp[delay:])

        return sum(dp)


        queue = collections.deque()
        queue.append(1)

        know_secret = 0

        for day in range(n-1):

            if len(queue) >= delay:
                people_share = sum(queue[:(delay)])

            if len(queue) >= forget:
                people_forget = queue.popleft()
