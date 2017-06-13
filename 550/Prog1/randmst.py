import sys
import random
import math


class UnionFind:
    def __init__(self):
        # Create a new empty union-find structure.
        self.weights = {}
        self.parents = {}

    def __getitem__(self, v):
        # Find and return the name of the set containing the object.
        # check for previously unknown object
        if v not in self.parents:
            self.parents[v] = v
            self.weights[v] = 1
            return v

        # find path of vertices leading to the root
        path = [v]
        root = self.parents[v]
        while root != path[-1]:
            path.append(root)
            root = self.parents[root]

        # compress the path and return
        for ancestor in path:
            self.parents[ancestor] = root
        return root

    def __iter__(self):
        # Iterate through all items ever found or unioned by this structure.
        return iter(self.parents)

    def union(self, *objects):
        # Find the sets containing the objects and merge them all.
        roots = [self[x] for x in objects]
        heaviest = max([(self.weights[r], r) for r in roots])[1]
        for r in roots:
            if r != heaviest:
                self.weights[heaviest] += self.weights[r]
                self.parents[r] = heaviest


def MST(G):
    # We use Kruskal's algorithm to return the minimum spanning tree of a graph G.
    # G should be represented in such a way that
    # - iter(G) lists its vertices
    # - iter(G[u]) lists the neighbors of u
    # - G[u][v] gives the length of edge u,v
    # - The tree is returned as a list of edges.
    subtrees = UnionFind()
    tree = []
    for w, u, v in sorted((G[u][v], u, v) for u in G for v in G[u]):
        if subtrees[u] != subtrees[v]:
            tree.append((u, v))
            subtrees.union(u, v)
    return tree


if __name__ == "__main__":
    if sys.argv[1] != "0" or len(sys.argv) != 5:
        print("Wrong Input Format! The first flag should be 0, and you should input 4 numbers in total.")
    if sys.argv[4] > "4" or sys.argv[4] == "1":
        print("Wrong Input Dimension! It can only be 0, 2, 3, and 4.")
    else:
        numpoints = sys.argv[2]
        numtrials = sys.argv[3]
        dimension = sys.argv[4]

    mst_weight = []
    n = int(numpoints)
    for i in range(int(numtrials)):
        G = {}
        for u in range(n):
            G[u] = {}

        if dimension == "0":
            for u in range(n):
                for v in range(u):
                    if v != u:
                        e = random.uniform(0, 1)
                        # throw away large edges for n >= 512
                        if n < 512 or e < math.log(n, 2) / n:
                            G[u][v] = e
                            G[v][u] = G[u][v]

        elif dimension == "2":
            for u in range(n):
                x1 = random.uniform(0, 1)
                y1 = random.uniform(0, 1)
                for v in range(u):
                    if v != u:
                        x2 = random.uniform(0, 1)
                        y2 = random.uniform(0, 1)
                        e = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
                        # save time for big values
                        if e < 2.0 / math.log(n, 2):
                            G[u][v] = e
                            G[v][u] = G[u][v]

        elif dimension == "3":
            for u in range(n):
                x1 = random.uniform(0, 1)
                y1 = random.uniform(0, 1)
                z1 = random.uniform(0, 1)
                for v in range(u):
                    if v != u:
                        x2 = random.uniform(0, 1)
                        y2 = random.uniform(0, 1)
                        z2 = random.uniform(0, 1)
                        e = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)
                        # save time for big values
                        if e < 3.0 / math.log(n, 2):
                            G[u][v] = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)
                            G[v][u] = G[u][v]

        elif dimension == "4":
            for u in range(n):
                x1 = random.uniform(0, 1)
                y1 = random.uniform(0, 1)
                z1 = random.uniform(0, 1)
                p1 = random.uniform(0, 1)
                for v in range(u):
                    if v != u:
                        x2 = random.uniform(0, 1)
                        y2 = random.uniform(0, 1)
                        z2 = random.uniform(0, 1)
                        p2 = random.uniform(0, 1)
                        e = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2 + (p1 - p2) ** 2)
                        # save time for big values
                        if e < 4.0 / math.log(n, 2):
                            G[u][v] = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2 + (p1 - p2) ** 2)
                            G[v][u] = G[u][v]

        T = MST(G)
        # print(len(T))
        mst_weight.append(sum([G[u][v] for u, v in T]))
    # print(mst_weight)
    # print(sum(mst_weight))
    print(sum(mst_weight)/(int(numtrials)), numpoints, numtrials, dimension)
