from typing import List
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        n = len(isConnected)
        visited = set()
        provinces = 0

        def check_provinces(i):
            stack = []
            stack.append(i)

            while stack:
                i = stack.pop()

                for j in range(n):
                    entry = isConnected[i][j]
                    new_key = str(i) + "_" + str(j)

                    if entry == 1:
                        if new_key not in visited:
                            visited.add(new_key)
                            stack.append(j)


        for i in range(n):
            key = str(i) + "_" + str(i)

            if key not in visited:
                provinces += 1
                visited.add(key)
                check_provinces(i)

        return provinces