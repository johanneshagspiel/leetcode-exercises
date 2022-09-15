class Solution:
    def validUtf8(self, data: List[int]) -> bool:

        mask_first_position = 1 << 7
        mask_second_position = 1 << 6

        n_bytes = 0

        for num in data:

            if n_bytes == 0:

                loop_mask = 1 << 7

                while loop_mask & num:
                    n_bytes += 1
                    loop_mask = loop_mask >> 1

                if n_bytes == 1 or n_bytes > 4:
                    return False

            else:

                if not (mask_first_position & num and not (mask_second_position & num)):
                    return False

            n_bytes -= 1

        return n_bytes == 0
