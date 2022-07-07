class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        s1_len = len(s1)
        s2_len = len(s2)
        s3_len = len(s3)

        if s1_len + s2_len != s3_len:
            return False

        self.found = False

        def rec_mem(s1_index, s2_index, s3_index, mem_dic):

            if s1_index == s1_len and s2_index == s2_len:
                self.found = True
                return True

            elif (s1_index, s2_index, s3_index) in mem_dic:
                return mem_dic[(s1_index, s2_index, s3_index)]

            elif s1_index == s1_len:
                if s2[s2_index] == s3[s3_index]:
                    result = rec_mem(s1_index, s2_index + 1, s3_index + 1, mem_dic)
                    mem_dic[(s1_index, s2_index, s3_index)] = result
                    return result
                else:
                    mem_dic[(s1_index, s2_index, s3_index)] = False
                    return False

            elif s2_index == s2_len:
                if s1[s1_index] == s3[s3_index]:
                    result = rec_mem(s1_index + 1, s2_index, s3_index + 1, mem_dic)
                    mem_dic[(s1_index, s2_index, s3_index)] = result
                    return result
                else:
                    mem_dic[(s1_index, s2_index, s3_index)] = False
                    return False

            else:

                if s1[s1_index] == s3[s3_index] and s2[s2_index] == s3[s3_index]:
                    result_1 = rec_mem(s1_index + 1, s2_index, s3_index + 1, mem_dic)
                    result_2 = rec_mem(s1_index, s2_index + 1, s3_index + 1, mem_dic)
                    result = result_1 or result_2
                    mem_dic[(s1_index, s2_index, s3_index)] = result
                    return result

                elif s1[s1_index] == s3[s3_index]:
                    result = rec_mem(s1_index + 1, s2_index, s3_index + 1, mem_dic)
                    mem_dic[(s1_index, s2_index, s3_index)] = result
                    return result

                elif s2[s2_index] == s3[s3_index]:
                    result = rec_mem(s1_index, s2_index + 1, s3_index + 1, mem_dic)
                    mem_dic[(s1_index, s2_index, s3_index)] = result
                    return result

                else:
                    mem_dic[(s1_index, s2_index, s3_index)] = False
                    return False

        rec_mem(0, 0, 0, {})
        return self.found
