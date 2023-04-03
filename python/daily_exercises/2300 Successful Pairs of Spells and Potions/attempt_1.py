class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:

        result = []

        potions.sort(reverse=True)

        for spell in spells:

            left = 0
            right = len(potions)

            temp_res = 0

            while left <= right:
                mid = left + ((right - left) // 2)
                mid_val = potions[mid]

                mid_success = mid_val * spell >= success
                next_position = mid + 1

                if next_position < len(potions):
                    next_val = potions[next_position]

                    next_success = next_val * spell >= success

                    if mid_success and not next_success:
                        temp_res = mid
                        break
                    elif not mid_success and not next_success:
                        right = mid - 1
                    else:
                        left = mid + 1

                else:
                    temp_res = len(potions)

            result.append(temp_res)

        return result

