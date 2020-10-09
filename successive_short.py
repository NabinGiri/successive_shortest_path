
import sys


class Dijkstra:
    def __init__(self, vertices):
        self.vertices = vertices
        self.dic = {}

    def p_sol(self, parent, node):
        self.p_list = []
        if parent[node] == -1:
            self.p_list.append(node)
            return
        self.p_sol(parent, parent[node])
        self.p_list.append(node)

    def sol(self, dist, parent):
        for node in range(self.vertices):
            self.p_sol(parent, node)
            self.dic[node] = [self.p_list, dist[node]]

    def min_distance(self, dist, sSet):
        mini = sys.maxsize
        for i in range(self.vertices):
            if dist[i] < mini and sSet[i] is False:
                mini = dist[i]
                min_index = i
        return min_index

    def dia_ago(self, graph, source):
        self.graph = graph
        dist = [sys.maxsize] * self.vertices
        parent = [-1] * self.vertices
        dist[source] = 0
        sSet = [False] * self.vertices
        for i in range(self.vertices):
            min_dis = self.min_distance(dist, sSet)
            sSet[min_dis] = True
            for j in range(self.vertices):
                if self.graph[min_dis][j] > 0 and sSet[j] is False and dist[j] > dist[min_dis] + self.graph[min_dis][j]:
                    dist[j] = dist[min_dis] + self.graph[min_dis][j]
                    parent[j] = min_dis
        self.sol(dist, parent)
        return self.dic

    def successive_short_path(self, matrix, source, dest):
        if self.dic is None:
            raise UserWarning("Call Dijkstra Algorithm first to identify the shortest path")
        initial_nodePath = self.dic[dest][0]
        initial_nodeCost = self.dic[dest][1]
        print("Number 1 lowest cost for destination", dest, "is:", initial_nodeCost, ", Path is:", initial_nodePath)
        current_node = source
        if current_node is dest:
            print("Source Node is Destination Node- Program Terminate")
            return 0
        for i in range(len(initial_nodePath) - 1):
            self.tempGraph = matrix
            self.tempGraph[initial_nodePath[i]][initial_nodePath[i + 1]] = sys.maxsize
            self.tempGraph[initial_nodePath[i + 1]][initial_nodePath[i]] = sys.maxsize
            ans = self.dia_ago(self.tempGraph, 0)
            print("Number", i + 2, "lowest cost for destination", dest, "is:", ans[dest][1], ", Path is:", ans[dest][0])


if __name__ == "__main__":
    g = Dijkstra(9)
    adj_matrix = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
                  [4, 0, 8, 0, 0, 0, 0, 11, 0],
                  [0, 8, 0, 7, 0, 4, 0, 0, 2],
                  [0, 0, 7, 0, 9, 14, 0, 0, 0],
                  [0, 0, 0, 9, 0, 10, 0, 0, 0],
                  [0, 0, 4, 14, 10, 0, 2, 0, 0],
                  [0, 0, 0, 0, 0, 2, 0, 1, 6],
                  [8, 11, 0, 0, 0, 0, 1, 0, 7],
                  [0, 0, 2, 0, 0, 0, 6, 7, 0]
                  ]
    source_node = 0
    destination_node = 6
    result = g.dia_ago(adj_matrix, source_node)
    print("Source node = ", source_node)
    print("Destination node = ", destination_node)
    print("Format = destination node:[[path],total cost] ")
    print(result)
    g.successive_short_path(adj_matrix, source_node, destination_node)

""" 
Notes:
Lets start with a graph having 9 vertices.
Suppose we have : Source Node = 0 and Destination Node = 6
After running Dijkstra algorithm, we identify the shortest path to reach destination node 6 is [0, 7, 6] with total cost 9.
Now, to find next shortest path, we formulate the below problems:
Shortest Path = [0, 7, 6]
Assume,
Problem 1: Cost(0,7) = infinity
Problem 2: Cost(7,6) = infinity
Now, the new shortest path are below:
[0, 1, 7, 6] with cost 16 and,
[0, 1, 2, 5, 6] with cost 18.

Steps:
1. Run a shortest path identifying algorithm (in our case, Dijkstra). Note: all the path cost are non-negative.
2. Find the shortest path. Find Optimal solution among feasible solutions
3. Once, the shortest path is identified, we retain the node path and create nodes-1 problems.
4. Run shortest path identifying algorithm again to identify the shortest path for each problem.

The shortest path identifying algorithm runs from source 0 to all nodes/vertices- just to see all the results.



"""
