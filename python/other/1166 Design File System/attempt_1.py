class Trie:

    def __init__(self):
        self.children = {}
        self.value = None

class FileSystem:

    def __init__(self):
        self.trie = Trie()

    def createPath(self, path: str, value: int) -> bool:
        path_list = path.split("/")[1:]

        if self._can_insert(path_list):

            trie = self.trie
            for path in path_list:
                if path not in trie.children:
                    trie.children[path] = Trie()
                trie = trie.children[path]
            trie.value = value

            return True

        else:
            return False


    def _can_insert(self, path_list):

        N = len(path_list)

        trie = self.trie

        for index, path in enumerate(path_list):
            if path in trie.children:
                trie = trie.children[path]
            else:
                if index == N - 1:
                    return True
                else:
                    return False



    def get(self, path: str) -> int:
        path_list = path.split("/")[1:]

        trie = self.trie
        for path in path_list:
            if path in trie.children:
                trie = trie.children[path]
            else:
                return -1

        return trie.value

