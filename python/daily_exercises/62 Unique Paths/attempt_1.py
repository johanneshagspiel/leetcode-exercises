class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        self.count = 0

        def walk(x, y):

            if x == m and y == m:
                self.count += 1

            else:

                if x < m:
                    walk(x+1, y)

                if y < n:
                    walk(x, y+1)

        walk(0, 0)
        
        return self.count
