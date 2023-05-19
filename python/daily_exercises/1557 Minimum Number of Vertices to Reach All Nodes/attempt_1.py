class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        allNodes = set()
        reachableNodes = set()

        for fromNode, toNode in edges:
            allNodes.add(fromNode)
            allNodes.add(toNode)
            reachableNodes.add(toNode)

        unreachableNodes = allNodes.difference(reachableNodes)

        return list(unreachableNodes)
