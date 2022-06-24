from typing import List
class Solution:
    def wordsAbbreviation(self, words: List[str]) -> List[str]:
        trie = {}
        trie["count"] = 0
        result_list = []

        for word in words:
            node = trie

            for i in word:
                if i not in node:
                    node[i] = {}
                    node[i]["count"] = 1
                node["count"] += 1
                node = node[i]

        for word in words:
            node = trie
            word_length = len(word)
            suffix_length = 0

            for i in word:
                current_node = node[i]
                current_count = current_node["count"]
                suffix_length += 1

                if current_count == 1:
                    break

            if (suffix_length >= (word_length - 2)):
                result_list.append(word)
            else:
                len_middle = word_length - suffix_length - 1
                new_word = word[:suffix_length] + str(len_middle) + word[-1:]
                result_list.append(new_word)

        return result_list
