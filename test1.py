#code made by Divyanshu Mehta
# adjustments made by Thomaz in order to print the step by step in terminal

from collections import defaultdict

class Graph():
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices
 
    def addEdge(self, u, v):
        self.graph[u].append(v)
 
    def isCyclicUtil(self, v, visited, recStack):
        # Mark current node as visited and adds to recursion stack
        print(f"visiting node {v}")
        visited[v] = True
        recStack[v] = True
 
        # Recur for all neighbours if any neighbour is visited and in
        # recStack then graph is cyclic
        for neighbour in self.graph[v]:
            print(f"checking neighbour {neighbour} of node {v}")
            if not visited[neighbour]:
                if self.isCyclicUtil(neighbour, visited, recStack):
                    return True
            elif recStack[neighbour]:
                print(f"back edge found from node {v} to node {neighbour}")
                return True
 
        # The node needs to be popped from recursion stack before function ends
        recStack[v] = False
        print(f"node {v} removed from recursion stack")
        return False
 
    # Returns true if graph is cyclic else false
    def isCyclic(self):
        visited = [False] * (self.V + 1)
        recStack = [False] * (self.V + 1)
        for node in range(self.V):
            if not visited[node]:
                if self.isCyclicUtil(node, visited, recStack):
                    return True
        return False

if __name__ == '__main__':
    g = Graph(14)
    g.addEdge(7, 0)
    g.addEdge(0, 8)
    g.addEdge(2, 8)
    g.addEdge(12, 5)
    g.addEdge(3, 8)
    g.addEdge(10, 3)
    g.addEdge(3, 9)
    g.addEdge(1, 9)
    g.addEdge(9, 4)
    g.addEdge(4, 11)
    g.addEdge(11, 6)
    g.addEdge(6, 10)


    if g.isCyclic():
        print("Graph contains cycle")
    else:
        print("Graph doesn't contain cycle")
