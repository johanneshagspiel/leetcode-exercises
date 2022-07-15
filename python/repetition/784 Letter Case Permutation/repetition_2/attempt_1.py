class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:

        bitmask = []
        for char in s:
            if char.isalpha():
                bitmask.append(1)
            else:
                bitmask.append(0)

        binary_mask = int("".join(bitmask))

        while binary_mask:
            position = binary_mask