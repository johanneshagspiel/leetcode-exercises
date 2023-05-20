class Solution:

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        gridWeight = {}

        def find(nodeId):

            if nodeId not in gridWeight:
                gridWeight[nodeId] = (nodeId, 1)

            groupId, nodeWeight = gridWeight[nodeId]

            if nodeId != groupId:
                newGroupdId, groupWeight = find(groupId)
                gridWeight[nodeId] = (newGroupdId, groupWeight * nodeWeight)

            return gridWeight[nodeId]

        def union(dividend, divisor, value):
            dividendId, dividendWeight = find(dividend)
            divisorId, divisorWeight = find(divisor)

            if dividendId != divisorId:
                gridWeight[dividendId] = (divisorId, divisorWeight * value / dividendWeight)

        for (dividend, divisor), value in zip(equations, values):
            union(dividend, divisor, value)

        results = []

        for dividend, divisor in queries:

            if dividend not in gridWeight or divisor not in gridWeight:
                results.append(-1)
            else:
                dividendId, dividendWeight = find(dividend)
                divisorId, divisorWeight = find(divisor)

                if dividendId != divisorId:
                    results.append(-1)
                else:
                    tempResult = dividendWeight / divisorWeight
                    results.append(tempResult)

        return results
