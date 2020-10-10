class SSP:

    def __init__(self, graph):
        self.graph = graph
        self.vertices = len(graph[0])
        self.tempGraph = [[self.graph[j][i] for j in range(self.vertices)] for i in range(self.vertices)]
        self.source = 0
        self.check = [False] * self.vertices
        self.flow = 0
        self.assign = []

    def node_potential(self):
        for i in range(self.vertices):
            path = (min(self.tempGraph[i]))
            self.reduce_weights(path, i)
        return self.flow, self.assign

    def reduce_weights(self, path, i):
        vals = []
        for j in range(self.vertices):
            weights = self.tempGraph[i][j] + self.source - path
            vals.append(weights)
        idx = vals.index(max(vals))
        while self.check[idx] is True:
            vals.pop(idx)
            idx = vals.index(max(vals))
        ans = self.tempGraph[i][idx]
        self.check[idx] = True
        self.assign.append(ans)
        self.flow += ans


if __name__ == "__main__":
    matrix = [[30, 40, 50, 60],
              [70, 30, 40, 70],
              [60, 50, 60, 30],
              [20, 80, 50, 70]]
    g = SSP(matrix)
    earning, steps = g.node_potential()
    print(earning)
    print(steps)

"""
Notes:
Problem Domain:
Input : Weighted complete bipartite graph matrix = (L U R, E) with |L| = |R|
Goal : Find a perfect matching of maximum weights


Input description: 
            A   B   C   D
Alice       30  40  50  60
Bob         70  30  40  70
Charlie     60  50  60  30
Diane       20  80  50  70

Here, we need to assign each workers, i.e Alice, Bob, Charlie, and Diane to one of the four tasks i.e A, B, C, D.
The matrix shows the earning of each workers per task.

Aim: Determine best matching of workers to earn maximum earning.

Approach: Successive Shortest Path
1. Successive Shortest Path has two main important parts:
a. Node Potential: In node potential section, we find the shortest path from source to a node. In our case, 
shortest path cost to task A, B, C, D.
Hence, we get
P(A) = Diane = 20
P(B) = Bob = 30
P(C) = Bob = 40
P(D) = Charlie = 30

b. Reduce Weights: The function we use is W(a,b) = W(a,b) + P(a) - P(b)
As such, we get;
For Task A:
W(Alice, A) = 30 + 0 - 20 = 10
W(Bob, A) = 70 + 0 - 20 = 50
W(Charlie, A) = 60 + 0 - 20 = 40
W(Diane, A) = 20 + 0 - 20 = 0

For Task B:
W(Alice, B) = 40 + 0 - 30 = 10
W(Bob, B) = 30 + 0 - 30 =  0
W(Charlie, B) = 50 + 0 - 30 = 20
W(Diane, B) = 80 + 0 - 30 = 50

For Task C:
W(Alice, C) = 50 + 0 - 40 = 10
W(Bob, C) = 40 + 0 - 40 = 0
W(Charlie, C) = 60 + 0  - 40 = 20
W(Diane, C) = 50 + 0 - 40 = 10

For Task D:
W(Alice, D) = 60 + 0 - 30 = 30
W(Bob, D) = 70 + 0 - 30 = 40
W(Charlie, D) = 30 + 0 - 30 = 0
W(Diane, D) = 70 + 0 - 30 = 40

Finally, we get the output from the program as :
Earning : 270
Matching : [70, 80, 60, 60]
Bob : A, Diane: B, Charlie : C, Alice: D.


Alternatively, if we want to check the minimum cost, we get:
Earning : 130
Matching : [20, 30, 50, 30]
Diane: A, Bob: B, Alice: C, Charlie: D

Improvement for the above program includes:
1. Implement Dijkstra Algorithm to identify node potentials.

"""