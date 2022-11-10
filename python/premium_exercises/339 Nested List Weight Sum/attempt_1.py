class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:

        def sum_at_position(depth, input_list):

            result = 0

            for nested_integer in input_list:

                if nested_integer.isInteger():
                    result += depth * nested_integer.getInteger()
                else:
                    result += sum_at_position(depth + 1, nested_integer.getList())

            return result

        return sum_at_position(1, nestedList)