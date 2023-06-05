# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):

        self.generator = self._int_generator(nestedList)
        self._peeked = None

    def _int_generator(self, nested_List):

        for element in nested_List:
            if element.isInteger():
                yield element.getInteger()
            else:
                yield from self._int_generator(element.getList())

    def next(self) -> int:
        if self.hasNext():
            result = self._peeked
            self._peeked = None
            return result
        else:
            return None

    def hasNext(self) -> bool:

        if self._peeked is not None:
            return True

        try:
            self._peeked = next(self.generator)
            return True
        except:
            return False
