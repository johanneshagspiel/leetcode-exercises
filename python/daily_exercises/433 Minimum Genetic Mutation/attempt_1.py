class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:

        bank_set = {word: True for word in bank}

        queue = collections.deque()
        queue.append((start, 0))

        seen_set = set()
        seen_set.add(start)

        while queue:

            len_queue = len(queue)

            for _ in range(len_queue):
                gene, moves = queue.popleft()

                if gene == end:
                    return moves
                else:
                    possible_char_set = {'A', 'C', 'G', 'T'}

                    for index, char in enumerate(gene):
                        alternative_set = possible_char_set.copy()
                        alternative_set.remove(char)

                        for alternative_char in alternative_set:
                            test_gene_list = list(gene)
                            test_gene_list[index] = alternative_char
                            test_gene = "".join(test_gene_list)

                            if test_gene in bank_set:
                                if test_gene not in seen_set:
                                    queue.append((test_gene, moves + 1))
                                    seen_set.add(test_gene)

        return -1
