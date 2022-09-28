class Solution:
    def pushDominoes(self, dominoes: str) -> str:

        n = len(dominoes)
        force_vector = [0 for _ in range(n)]

        force = 0
        for position in range(n):
            domino = dominoes[position]

            if domino == 'R':
                force = n
            elif domino == 'L':
                force = 0
            else:
                force = max(0, force - 1)

            force_vector[position] += force

        force = 0
        for position in range(n - 1, -1, -1):
            domino = dominoes[position]

            if domino == 'L':
                force = n
            elif domino == 'R':
                force = 0
            else:
                force = max(0, force - 1)

            force_vector[position] -= force

        res = ""
        for position in range(n):
            force = force_vector[position]

            if force > 0:
                res += 'R'
            elif force < 0:
                res += 'L'
            else:
                res += '.'

        return res
