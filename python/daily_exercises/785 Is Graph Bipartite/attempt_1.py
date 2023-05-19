class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        setA = set()
        setB = set()

        def checkOption(vertex):

            if vertex >= len(graph):
                return True
            else:
                edges = graph[vertex]

                if vertex in setB:
                    for otherVertex in edges:
                        if otherVertex in setB:
                            return False
                        else:
                            setA.add(otherVertex)

                    return

                elif vertex in setA:
                    for otherVertex in edges:
                        if otherVertex in setA:
                            return False
                        else:
                            setB.add(otherVertex)

                else:
                    setA.add(vertex)
                    option1 = checkOption(vertex + 1)
                    setA.remove(vertex)

                    setB.add(vertex)
                    option2 = checkOption(vertex + 1)
                    setB.remove(vertex)

                    finalResult = option1 or option2
                    return finalResult


