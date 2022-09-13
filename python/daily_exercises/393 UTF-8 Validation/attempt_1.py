from typing import Optional, List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:

        first_byte = bin(data[0])[2:]

        padding_needed = 8 - len(first_byte)

        if padding_needed > 0:
            padding = [0 for _ in range(padding_needed)]
            padding.extend(first_byte)
            first_byte = padding

        one_count = 0

        for char in first_byte:
            if char == "1":
                one_count += 1
            else:
                break

        other_bytes = data[1:]

        if one_count == 1 or len(other_bytes) != max(0, one_count - 1):
            return False

        continuation_bytes = other_bytes[:(one_count - 1)]

        for byte in continuation_bytes:
            string_byte = bin(byte)[2:]

            padding_needed = 8 - len(string_byte)

            if padding_needed > 0:
                padding = [0 for _ in range(padding_needed)]
                padding.extend(string_byte)
                string_byte = padding

            one_count = 0

            for char in string_byte:
                if char == "1":
                    one_count += 1
                else:
                    break

            if one_count != 1:
                return False

        return True
