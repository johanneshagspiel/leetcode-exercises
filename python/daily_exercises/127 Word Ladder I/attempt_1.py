import collections


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:

        pre_dic = {}

        wordList.append(beginWord)

        for word in wordList:

            for position in range(len(word)):
                temp_word = list(word[::])
                temp_word[position] = '*'
                temp_word = "".join(temp_word)

                if temp_word not in pre_dic:
                    pre_dic[temp_word] = []
                pre_dic[temp_word].append(word)

        seen = set()
        queue = collections.deque()
        queue.append((beginWord, 1))

        while queue:

            size = len(queue)

            for element in range(size):

                word, level = queue.popleft()

                if word == endWord:
                    return level
                else:

                    possible_transformations = []

                    for position in range(len(word)):
                        temp_word = list(word[::])
                        temp_word[position] = '*'
                        temp_word = "".join(temp_word)
                        possible_transformations.append(temp_word)

                    for possible_transformation in possible_transformations:
                        options = pre_dic[possible_transformation]

                        for option in options:
                            if option not in seen:
                                seen.add(option)
                                queue.append((option, level + 1))

        return 0

