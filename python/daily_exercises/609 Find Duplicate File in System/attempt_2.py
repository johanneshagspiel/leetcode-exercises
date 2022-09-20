import collections
from typing import List


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:

        path_dic = collections.defaultdict(list)

        for element in paths:
            element_list = element.split(" ")
            path = element_list[0]
            content_list = element_list[1:]

            for content in content_list:
                file_name = content.split('(')[0]
                key_content = content.split('(')[1][:-1]

                file_path = str(path) + "/" + str(file_name)

                path_dic[key_content].append(file_path)

        solution = []

        for key_content, file_path_list in path_dic.items():

            if len(file_path_list) > 1:
                solution.append(file_path_list)

        return solution
