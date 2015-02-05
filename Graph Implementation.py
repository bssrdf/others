# google

# directed graph
class Graph(object):
    # constrcutor
    def __init__(self):
        self.vertices = {}

    # add vertex
    def addVertex(self, node):
        self.vertices[node] = []

    # add edge
    def addEdge(self, pair):
        self.vertices[pair[0]].append(pair[1])

    # dfs traversal
    def dfs(self, start):
        res = []; visited = set([]); stack = [start]
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                res.append(node)
                for adj in self.vertices[node]:
                    stack.append(adj)
        return res

    # bfs traversal
    def bfs(self, start):
        res = []; currents = [start]; visited = set([])
        while currents:
            node = currents.pop(0)
            if node not in visited: 
                visited.add(node)
                res.append(node)
                for adj in self.vertices[node]:
                    currents.append(adj)
        return res

    # if or not bipartite
    def isBipartite(self, start):
        colors = {i:0 for i in self.vertices.keys()}
        currents = [start]; colors[start] = 1
        while currents:
            node = currents.pop(0)
            for adj in self.vertices[node]:
                if colors[adj] == 0:
                    colors[adj] = 1 if (colors[node] == -1) else -1
                    currents.append(adj)
                elif colors[adj] == colors[node]:
                    return False
        return True

    # if or not having cycle
    def hasCycle(self):
        visited = {i:False for i in self.vertices.keys()}
        recstack = {i:False for i in self.vertices.keys()}
        for node in self.vertices.keys():
            if self.cycle(node, visited, recstack): return True
        return False

    def cycle(self, start, visited, recstack):
        if visited[start] == False:
            visited[start] = True
            recstack[start] = True
            for adj in self.vertices[start]:
                if visited[adj] == False and self.cycle(adj, visited, recstack):
                    return True
                elif recstack[adj]:
                    return True
        recstack[start] = False
        return False

    # topological sort
    def topologicalSort(self):
        visited = {i:False for i in self.vertices.keys()}
        stack = []
        for i in self.vertices.keys():
            if visited[i]==False: self.topologicalSortRecur(i, visited, stack)
        res = list(reversed(stack))
        return res

    def topologicalSortRecur(self, node, visited, stack):
        visited[node] = True
        for adj in self.vertices[node]:
            if visited[adj] == False: self.topologicalSortRecur(adj, visited, stack)
        stack.append(node)

    # if or not strongly connected
    

if __name__ == "__main__":
    g = Graph()    
    g.addVertex(1); g.addVertex(2); g.addVertex(3); g.addVertex(4); g.addVertex(5);  
    g.addEdge((1,2)); g.addEdge((2,3)); g.addEdge((3,4)); g.addEdge((3,5)); 
    print g.vertices
    print g.dfs(1)
    print g.bfs(1)
    print g.isBipartite(1)
    print g.hasCycle()
    print g.topologicalSort()




































