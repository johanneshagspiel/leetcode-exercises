class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        people.sort(reverse = True)

        boats_needed = 0

        left = 0
        right = len(people) - 1

        while left <= right:

            combined_weight = people[left] + people[right]

            if combined_weight <= limit:
                boats_needed += 1
                left += 1
                right -= 1
            else:
                boats_needed += 1
                left += 1

        return boats_needed
