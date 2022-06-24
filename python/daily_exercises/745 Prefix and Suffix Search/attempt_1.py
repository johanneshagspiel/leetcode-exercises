import re
from typing import List
class WordFilter:

    def __init__(self, words: List[str]):
        self.search_string = ""
        current_index = 0

        for word in words:
            additional_string = word + ":" + str(current_index) + "#"
            self.search_string += additional_string
            current_index += 1

    def f(self, prefix: str, suffix: str) -> int:
        result = re.findall(f"[^{prefix}].*", self.search_string)
        return result

if __name__ == "__main__":

    wordFilter = WordFilter(["apple", "able"])
    print(wordFilter.f("a", "e"))