class Solution:
    def minDeletions(self, s: str) -> int:

        frequencies = [0 for _ in range(26)]

        for char in s:
            frequencies[ord(char) - 97] += 1

        frequencies.sort(reverse=True)

        deletions = 0
        largest_freq = frequencies[0]

        for frequency in frequencies[1:]:
            if frequency >= largest_freq:
                target_amount = max(0, largest_freq - 1)
                del_needed = frequency - target_amount

                frequency = target_amount
                deletions += del_needed

            largest_freq = frequency

        return deletions