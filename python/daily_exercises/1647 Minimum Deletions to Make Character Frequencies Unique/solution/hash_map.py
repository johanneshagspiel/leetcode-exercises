class Solution:
    def minDeletions(self, s: str) -> int:

        frequencies = [0 for _ in range(26)]

        for char in s:
            frequencies[(ord(char) - 97)] += 1

        deletions = 0
        seen_frequencies = set()

        for index in range(26):

            while frequencies[index] > 0 and frequencies[index] in seen_frequencies:
                frequencies[index] -= 1
                deletions += 1

            seen_frequencies.add(frequencies[index])

        return deletions
