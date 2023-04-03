class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        word_1_position_dic = {}
        word_2_position_dic = {}

        for index, word in enumerate(wordsDict):
            if word == word1:
                word_1_position_dic[index]= True
            elif word == word2:
                word_2_position_dic[index]= True

        if word1 == word2:
            word_1_position_dic = word_2_position_dic

        min_distance = float("inf")

        prev_start_1 = -3
        prev_start_2 = -2
        final_word_1_position_dic = {}
        for index_1 in word_1_position_dic.keys():

            if prev_start_2 in final_word_1_position_dic and prev_start_2 + 1 == index_1:
                final_word_1_position_dic.pop(index_1 - 1)
                final_word_1_position_dic[index_1] = True
            else:
                final_word_1_position_dic[index_1] = True

            prev_start_1 = prev_start_2
            prev_start_2 = index_1