class SparseVector:
    def __init__(self, nums: List[int]):
        self.sparse_dic = {}

        for index, num in enumerate(nums):
            self.sparse_dic[index] = num


    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0

        sparse_dic_2 = vec.sparse_dic

        for index_1, num_1 in self.sparse_dic.items():
            if index_1 in sparse_dic_2:
                res += num_1 * sparse_dic_2[index_1]

        return res

