class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.list = []
        self.k = k

        for num in nums:
            self._add(num)

    def add(self, val: int) -> int:
        self._add(val)
        return self.list[len(self.list) - self.k]

    def _add(self, val):

        if len(self.list) == 0:
            self.list.append(val)
        else:
            self.list.append(val)

            stop_index = max(0, len(self.list) - self.k - 2)
            compare_index = len(self.list) - 1

            for index in range(len(self.list)-2, stop_index, -1):
                curNum = self.list[index]
                compareVal = self.list[compare_index]

                if compareVal < curNum:
                    self.list[index], self.list[compare_index] = self.list[compare_index], self.list[index]
                    compare_index -= 1
                else:
                    break


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)