import string
from typing import List

class Trie_Node():

    def __init__(self):
        self.children = {}
        self.word = False

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:

        trie = Trie_Node()
        result_list = []

        for product in products:
            node = trie
            for i in product:
                if i not in node.children:
                    node.children[i] = Trie_Node()
                node = node.children[i]
            node.word = True

        len_search_word = len(searchWord)

        for end_index in range(len_search_word):
            prefix = searchWord[:(end_index + 1)]

            prefix_wrong = False

            node = trie
            for i in prefix:
                if i in node.children:
                    node = node.children[i]
                else:
                    prefix_wrong = True
                    break

            if prefix_wrong:
                result_list.append([])
            else:
                start_word = prefix
                self.result =[]
                self.dfs(node, start_word)
                result_list.append(self.result)

        return result_list

    def dfs(self, root, word):

        if len(self.result) == 3:
            return

        if root.word:
            self.result.append(word)

        for char in string.ascii_lowercase:
            if char in root.children:
                self.dfs(root.children[char], word + char)

if __name__ == "__main__":
    solution = Solution()
    print(solution.suggestedProducts(products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"))