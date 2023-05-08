class Solution:
    def average(self, salary: List[int]) -> float:

        minNum = float("inf")
        maxNum = -float("inf")

        for num in salary:
            minNum = min(minNum, num)
            maxNum = max(maxNum, num)

        runSum = 0
        count = 0

        for num in salary:
            if num != minNum and num != maxNum:
                runSum += num
                count += 1

        avgNum = runSum / count

        return avgNum
