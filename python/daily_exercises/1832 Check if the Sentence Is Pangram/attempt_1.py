class Solution:
    def checkIfPangram(self, sentence: str) -> bool:

        alphabet_counter = [1 for _ in range(26)]

        for char in sentence:
            char_index = ord(char) - ord("a")

            if alphabet_counter[char_index] != 0:
                alphabet_counter[char_index] -= 1

        return sum(alphabet_counter) == 0

