from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:

        transformation_array = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        res_dic = {}

        for word in words:
            curr_trans = ""

            for char in word:
                char_index = ord(char) - ord('a')
                curr_trans += transformation_array[char_index]

            res_dic[curr_trans] = True

        return len(res_dic.keys())


