class Solution:
    def reverseVowels(self, s: str) -> str:
        str_list = list(s)
        vowel_queue = collections.deque()
        index_list = []

        for index, char in enumerate(str_list):
            if char.lower() in ['a', 'e', 'i', 'o', 'u']:
                vowel_queue.appendleft(char)
                index_list.append(index)

        for index in index_list:
            str_list[index] = vowel_queue.popleft()

        return "".join(str_list)
