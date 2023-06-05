import collections


class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:

        delay_queue = collections.deque()
        delay_queue.append(1)

        forget_queue = collections.deque()
        forget_queue.append(1)

        share_secret = 0

        for day in range(n-1):

            if len(delay_queue) >= delay:
                share_secret += delay_queue.popleft()

            if len(forget_queue) >= forget:
                share_secret -= forget_queue.popleft()

            delay_queue.append(share_secret)
            forget_queue.append(share_secret)

        return share_secret % (pow(10, 9) + 7)