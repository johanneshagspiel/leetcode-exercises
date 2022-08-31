import itertools


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:

        permuatations = itertools.permutations(str(n))

        for perm in permuatations:
            if perm[0] != '0':
                bin = int("".join(perm))

                if bin & (bin - 1) == 0:

                    return True

        return False
