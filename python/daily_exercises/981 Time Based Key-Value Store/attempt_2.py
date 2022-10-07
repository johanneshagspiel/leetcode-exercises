class TimeMap:

    def __init__(self):
        self.dic = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.dic:
            return ""
        else:
            entries = self.dic[key]

            if timestamp < entries[0][0]:
                return ""
            else:
                left = 0
                right = len(entries)

                while left < right:
                    mid = left + ((right - left) // 2)

                    if entries[mid][0] <= timestamp:
                        left = mid + 1
                    else:
                        right = mid

            return entries[right - 1][1]
