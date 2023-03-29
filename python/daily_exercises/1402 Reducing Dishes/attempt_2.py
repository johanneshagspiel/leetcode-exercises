class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:

        num_dishes = len(satisfaction)
        satisfaction.sort()

        total_satisfaction = 0
        max_satisfaction = 0

        for index in range(num_dishes - 1, -1, -1):
            if satisfaction[index] + total_satisfaction > 0:
                total_satisfaction += satisfaction[index]
                max_satisfaction += total_satisfaction

        return max_satisfaction
