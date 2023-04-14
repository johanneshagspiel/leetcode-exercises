class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        word_1_position_list = []
        word_2_position_list = []

        for index, word in enumerate(wordsDict):
            if word == word1:
                word_1_position_list.append(index)
            elif word == word2:
                word_2_position_list.append(index)

        if word1 == word2:
            word_2_position_list = word_1_position_list

        min_distance = len(wordsDict)
        cur_word_2_position = 0
        max_word_2_position = len(word_2_position_list) - 1

        for word_1_position in word_1_position_list:

            keep_going = True
            distance = 0
            while keep_going and cur_word_2_position < len(word_2_position_list):

                while word_2_position_list[cur_word_2_position] == word_1_position:
                    cur_word_2_position += 1

                word_2_position_1 = word_2_position_list[cur_word_2_position]
                word_2_position_2 = len(wordsDict)
                if cur_word_2_position < max_word_2_position:
                    word_2_position_2 = word_2_position_list[cur_word_2_position + 1]

                distance_1 = abs(word_2_position_1 - word_1_position)
                distance_2 = abs(word_2_position_2 - word_1_position)

                distance = min(distance_1, distance_2)

                if distance_2 < distance_1:
                    cur_word_2_position += 1
                else:
                    keep_going = False

            if distance != 0:
                min_distance = min(min_distance, distance)

        return min_distance
