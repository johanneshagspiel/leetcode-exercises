class Solution(object):
    def minChanges(self, s):
        """
        :type s: str
        :rtype: int
        """

        compare_char = ''
        count = 0
        changes = 0

        for i in range(len(s)):
            current_char = s[i]

            if i % 2 == 0:
                compare_char = current_char
                count = 1
            else:
                if compare_char != current_char:
                    changes += 1
                count += 1

        return changes
