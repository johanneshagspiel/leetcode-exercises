class Solution:
    def pushDominoes(self, dominoes: str) -> str:

        N = len(dominoes)

        force_vector = [0 for _ in range(N)]

        force = 0
        for position in range(N):

            if dominoes[position] == "R":
                force = N
            elif dominoes[position] == "L":
                force = 0
            else:
                force = max(force - 1, 0)

            force_vector[position] += force

        force = 0
        for position in range(N-1, -1, -1):

            if dominoes[position] == "L":
                force = N
            elif dominoes[position] == "R":
                force = 0
            else:
                force = max(force - 1, 0)

            force_vector[position] -= force

        ans = ""
        for position in range(N):
            force = force_vector[position]

            if force == 0:
                ans += "."
            elif force < 0:
                ans += "L"
            else:
                ans += "R"

        return ans
