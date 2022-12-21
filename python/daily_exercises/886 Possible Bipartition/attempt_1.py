class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:

        not_found = True

        def rec_part(i, set_1, set_2):

            nonlocal not_found

            if i == len(dislikes):
                not_found = False

            else:
                num_1, num_2 = dislikes[i]

                if not_found:

                    if (num_1 not in set_1) and (num_2 not in set_2):
                        if num_1 not in set_2:
                            set_1.add(num_1)

                        if num_2 not in set_1:
                            set_2.add(num_2)

                        rec_part(i + 1, set_1, set_2)

                        if num_1 in set_1:
                            set_1.remove(num_1)

                        if num_2 in set_2:
                            set_2.remove(num_2)

                if not_found:

                    if (num_1 not in set_1) and (num_2 not in set_1):
                        if num_1 not in set_2:
                            set_1.add(num_1)

                        if num_2 not in set_2:
                            set_1.add(num_1)

                        rec_part(i + 1, set_1, set_2)

                        if num_1 in set_1:
                            set_1.remove(num_1)

                        if num_2 in set_1:
                            set_1.remove(num_2)

                if not_found:

                    if (num_1 not in set_2) and (num_2 not in set_2):
                        if num_1 not in set_1:
                            set_2.add(num_1)

                        if num_2 not in set_1:
                            set_2.add(num_2)

                        rec_part(i + 1, set_1, set_2)

                        if num_1 in set_2:
                            set_2.remove(num_1)

                        if num_2 in set_2:
                            set_2.remove(num_2)

                if not_found:

                    if (num_1 not in set_2) and (num_2 not in set_1):
                        if num_1 not in set_1:
                            set_2.add(num_1)

                        if num_2 not in set_2:
                            set_1.add(num_2)

                        rec_part(i + 1, set_1, set_2)

                        if num_1 in set_2:
                            set_2.remove(num_1)

                        if num_2 in set_1:
                            set_1.remove(num_2)

        rec_part(0, set(), set())

        return (not not_found)
