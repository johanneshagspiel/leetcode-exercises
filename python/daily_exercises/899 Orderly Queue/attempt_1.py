class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:

        if k == 1:

            options = [s]
            s_list = list(s)
            for _ in range(len(s)):
                pos_0 = s_list.pop(0)
                s_list.append(pos_0)
                options.append("".join(s_list))

            return min(options)

        else:
            return "".join(sorted(s))
        