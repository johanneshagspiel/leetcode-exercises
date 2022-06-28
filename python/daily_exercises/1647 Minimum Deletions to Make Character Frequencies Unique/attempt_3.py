class Solution:
    def minDeletions(self, s: str) -> int:

        frequencies = [0 for _ in range(26)]

        for char in s:
            frequencies[ord(char) - 97] += 1

        frequencies.sort(reverse=True)

        deletions = 0
        last_seen_frequencies = frequencies[0]

        for frequency in frequencies[1:]:

            if frequency == 0:
                break
            else:
                if last_seen_frequencies <= frequency:
                    target_amount = max(last_seen_frequencies - 1, 0)
                    del_needed = frequency - target_amount

                    deletions += del_needed
                    frequency = target_amount

                last_seen_frequencies = frequency

        return deletions
