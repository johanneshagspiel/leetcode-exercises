class Solution:
    def frequencySort(self, s: str) -> str:

        frequency_counter = collections.Counter(s)
        max_freq = max(frequency_counter.values())
        bucket = [[] for _ in range(max_freq + 1)]

        for letter, freq in frequency_counter.items():
            bucket[freq].append(letter)

        res = ""
        for i in range(len(bucket) - 1, -1, -1):
            letter_list = bucket[i]

            if len(letter_list) > 0:
                for char in letter_list:
                    res += (char * i)

        return res