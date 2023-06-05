import collections


class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:

        n = len(messages)
        sender_dic = collections.defaultdict(int)

        max_len = 0
        max_sender = None

        for index in range(n):
            sender = senders[index]
            word_length = len(messages[index].split(" "))

            sender_dic[sender] += word_length
            sender_word_count = sender_dic[sender]

            if sender_word_count > max_len:
                max_len = sender_word_count
                max_sender = sender

            if sender_word_count == max_len:
                if sender < max_sender:
                    max_len = sender_word_count
                    max_sender = sender

        return max_sender
