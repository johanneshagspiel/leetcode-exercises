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

        def _create_generator(nestedList):

            for element in nestedList:
                if element.isInteger():
                    yield element.getInteger()
                else:
                    yield from _create_generator(element.getList())

        self.generator = _create_generator(nestedList)
        self.peeked = None

    def next(self) -> int:

        if self.hasNext():
            current_element = self.peeked
            self.peeked = None
            return current_element

        else:
            return None

    def hasNext(self) -> bool:

        if self.peeked is not None:
            return True

        else:
            try:
                self.peeked = next(self.generator)
                return True
            except:
                return False
