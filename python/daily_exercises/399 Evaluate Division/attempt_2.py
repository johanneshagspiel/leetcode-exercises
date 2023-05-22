class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        nodeGrid = {}

        def find(nodeId):

            if nodeId not in nodeGrid:
                nodeGrid[nodeId] = (nodeId, 1)

            groupId, groupWeight = nodeGrid[nodeId]

            if groupId != nodeId:
                newGroupId, newGroupWeight = find(groupId)
                nodeGrid[nodeId] = (newGroupId, newGroupWeight * groupWeight)

            return nodeGrid[nodeId]

        def union(dividend, divisor, value):

            dividendId, dividendWeight = find(dividend)
            divisorId, divisorWeight = find(divisor)

            if divisorId != dividendId:
                nodeGrid[dividendId] = (divisorId, divisorWeight * (value / dividendWeight))

        for (divisor, dividend), value in zip(equations, values):
            union(divisor, dividend, value)

        results = []

        for divisor, dividend in queries:
            if divisor not in nodeGrid or dividend not in nodeGrid:
                results.append(-1)
            else:
                divisorId, divisorWeight = find(divisor)
                dividendId, dividendWeight = find(dividend)

                if divisorId != dividendId:
                    results.append(-1)
                else:
                    tempResult = divisorWeight / dividendWeight
                    results.append(tempResult)

        return results
