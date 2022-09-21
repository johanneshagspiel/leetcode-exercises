import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        queue = collections.deque()

        s_counter = collections.Counter(s)
        t_counter = collections.defaultdict(int)

        needed = len(s_counter)
        formed = 0

        right = 0
        left = 0

        min_substring = 0
        ans = ""

        while right < len(s):

            right_char = s[right]

            if right_char

