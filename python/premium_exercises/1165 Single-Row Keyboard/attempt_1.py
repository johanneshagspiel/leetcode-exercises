class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:

        char_to_ind = [0] * 26
        keyboard_list = list(keyboard)

        for index, char in enumerate(keyboard_list):
            char_to_ind[ord(char) - ord('a')] = index

        currentPos = 0
        totalMove = 0

        word_list = list(word)

        for char in word_list:
            target_position = char_to_ind[ord(char) - ord('a')]
            moves = abs(currentPos - target_position)
            totalMove += moves
            currentPos = target_position

        return totalMove
