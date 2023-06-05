import collections


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):

        def flattenList(cur_list):

            res = []
            for element in cur_list:

                if element.isInteger():
                    res.append(element.getInteger())
                else:
                    res.extend(flattenList(element.getList()))

            return res

        self.nested_queue = collections.deque()

        for element in nestedList:
            if element.isInteger():
                self.nested_queue.append(element.getInteger())
            else:
                pass
                cur_list = element.getList()
                flat_list = flattenList(cur_list)

                for list_el in flat_list:
                    self.nested_queue.append(list_el)




    def next(self) -> int:
        return self.nested_queue.popleft()


    def hasNext(self) -> bool:
        if len(self.nested_queue) == 0:
            return False
        else:
            return True
