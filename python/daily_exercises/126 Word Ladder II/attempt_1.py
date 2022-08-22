from typing import List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:

        def get_distance(word_1, word_2):

            dif = 0

            for position in range(len(word_1)):
                if word_1[position] != word_2[position]:
                    dif += 1

            return dif


        wordList.append(beginWord)

        n = len(wordList)
        dp = [[0]*n for _ in range(n)]

        index_dic = {}
        word_dic = {}

        for position in range(n):

            cur_word = wordList[position]

            for index, word in enumerate(wordList):
                cur_distance = get_distance(word, cur_word)
                goal_distance = get_distance(endWord, cur_word)
                dp[position][index] = cur_distance, goal_distance

                if position == 0:
                    index_dic[word] = index
                    word_dic[index] = word

        if endWord not in index_dic:
            return []

        else:


            end_index = index_dic[endWord]
            start_index = index_dic[beginWord]

            self.res = []
            self.min_len = float("inf")

            def rec_mem(cur_list, cur_index, cur_goal_dif, position_set):

                if cur_index == end_index:
                    cur_len = len(cur_list)

                    if cur_len < self.min_len:
                        self.min_len = cur_len
                        self.res = []
                        self.res.append(cur_list[::])
                    elif cur_len == self.min_len:
                        self.res.append(cur_list[::])

                else:
                    cur_options = dp[cur_index]

                    for new_index in range(len(cur_options)):
                        cur_distance, goal_distance = cur_options[new_index]

                        if cur_distance == 1 and new_index not in position_set and goal_distance < cur_goal_dif:
                            position_set.add(new_index)
                            cur_list.append(word_dic[new_index])

                            rec_mem(cur_list, new_index, position_set)

                            position_set.remove(new_index)
                            cur_list.pop()

            rec_mem([word_dic[start_index]], start_index, get_distance(beginWord, endWord), {start_index})
            return self.res
