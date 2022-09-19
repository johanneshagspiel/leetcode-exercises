import collections
import math
from typing import List


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:

        content_dic = collections.defaultdict(list)

        split_list = [x.split(" ") for x in paths]

        for element in split_list:
            path = element[0]
            content_list = element[1:]

            for content in content_list:
                file_name = content.split('(')[0]
                file_content = content.split('(')[1][:-1]

                file_path = path + "/" + file_name

                content_dic[file_content].append(file_path)

        res = []

        for file_content, path_list in content_dic.items():
            if len(path_list) > 1:
                res.append(path_list)

        math.log10()

        return res
