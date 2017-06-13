import sys
import random
import math
import time




class UnionFind:
    def __init__(self):
        """Create a new empty union-find structure."""
        self.weights = {}
        self.parents = {}

    def __getitem__(self, v):
        """Find and return the name of the set containing the object."""
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
        """Iterate through all items ever found or unioned by this structure."""
        return iter(self.parents)

    def union(self, *objects):
        """Find the sets containing the objects and merge them all."""
        roots = [self[x] for x in objects]
        heaviest = max([(self.weights[r], r) for r in roots])[1]
        for r in roots:
            if r != heaviest:
                self.weights[heaviest] += self.weights[r]
                self.parents[r] = heaviest


def MST(G):
    """
    We use Kruskal's algorithm to return the minimum spanning tree of a graph G.
    G should be represented in such a way that
    iter(G) lists its vertices
    iter(G[u]) lists the neighbors of u
    G[u][v] gives the length of edge u,v
    The tree is returned as a list of edges.
    """
    subtrees = UnionFind()
    tree = []
    for w, u, v in sorted((G[u][v], u, v) for u in G for v in G[u]):
        if subtrees[u] != subtrees[v]:
            tree.append((u, v))
            subtrees.union(u, v)
    return tree


if __name__ == "__main__":
    # if sys.argv[1] != "0" or len(sys.argv) != 5:
    #     print("Wrong Input Format!")
    # if sys.argv[4] > "4" or sys.argv[4] == "1":
    #     print("Wrong Input Dimension!")
    # else:
    #     numpoints = sys.argv[2]
    #     numtrials = sys.argv[3]
    #     dimension = sys.argv[4]

    dimension = sys.argv[1]

    # n = int(numpoints)
    n = [16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16348]
    print(list(n))

    for j in n:
        t0 = time.time()
        mst_weight = []
        for i in range(1):
            G = {}
            for u in range(j):
                G[u] = {}

            if dimension == "0":
                for u in range(j):
                    for v in range(u):
                        if v != u:
                            e = random.uniform(0, 1)
                            # save time for big values
                            if e < math.log(j, 2)/j:
                                G[u][v] = e
                                G[v][u] = G[u][v]


            elif dimension == "2":
                for u in range(j):
                    x1 = random.uniform(0, 1)
                    y1 = random.uniform(0, 1)
                    for v in range(u):
                        if v != u:
                            x2 = random.uniform(0, 1)
                            y2 = random.uniform(0, 1)
                            e = math.sqrt((x1-x2) ** 2 + (y1-y2) ** 2)
                            # save time for big values
                            if e < 2.0/math.log(j, 2):
                                G[u][v] = e
                                G[v][u] = G[u][v]


            elif dimension == "3":
                for u in range(j):
                    x1 = random.uniform(0, 1)
                    y1 = random.uniform(0, 1)
                    z1 = random.uniform(0, 1)
                    for v in range(u):
                        if v != u:
                            x2 = random.uniform(0, 1)
                            y2 = random.uniform(0, 1)
                            z2 = random.uniform(0, 1)
                            e = math.sqrt((x1-x2) ** 2 + (y1-y2) ** 2 + (z1-z2) ** 2)
                            # save time for big values
                            if e < 3.0/math.log(j, 2):
                                G[u][v] = math.sqrt((x1-x2) ** 2 + (y1-y2) ** 2 + (z1-z2) ** 2)
                                G[v][u] = G[u][v]


            elif dimension == "4":
                for u in range(j):
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
                            e = math.sqrt((x1-x2) ** 2 + (y1-y2) ** 2 + (z1-z2) ** 2 + (p1-p2) ** 2)
                            # save time for big values
                            if e < 4.0/math.log(j, 2):
                                G[u][v] = math.sqrt((x1-x2) ** 2 + (y1-y2) ** 2 + (z1-z2) ** 2 + (p1-p2) ** 2)
                                G[v][u] = G[u][v]


            t1 = time.time()
            T = MST(G)
            # print(T)
            # print(len(T))
            mst_weight.append(sum([G[u][v] for u, v in T]))
            t2 = time.time()
        # print(mst_weight)
        # print(sum(mst_weight))
        # print(j, ",", sum(mst_weight)/1, ",", dimension, ",")
        print(j, ",", t2 - t1, ",", t2 - t0, ",", dimension, ",")



"""
16 , 1.0672175884029664 , 0 ,
32 , 1.2079181268110901 , 0 ,
64 , 1.1257097265748204 , 0 ,
128 , 1.0867685637986477 , 0 ,
256 , 1.1806702971405165 , 0 ,
512 , 1.2537026183641438 , 0 ,
1024 , 1.1931837956477647 , 0 ,
2048 , 1.2095507211312981 , 0 ,
4096 , 1.2102387130089962 , 0 ,
8192 , 1.196066568913348 , 0 ,
16348 , 1.1937450661426692 , 0 ,

"""
"""
16 , 2.2634525292386463 , 2 ,
32 , 3.3271439476467557 , 2 ,
64 , 4.709684116052539 , 2 ,
128 , 6.228814676600714 , 2 ,
256 , 9.567379745441391 , 2 ,
512 , 13.115966864030796 , 2 ,
1024 , 17.84070129748393 , 2 ,
2048 , 25.773743834348107 , 2 ,
4096 , 36.520109861811186 , 2 ,
8192 , 51.758265571358315 , 2 ,
16384, 73.39686387247293 , 2 ,
"""
"""
16 , 3.598967422755377 , 3 ,
32 , 6.756670403646506 , 3 ,
64 , 10.431007308577867 , 3 ,
128 , 16.31915988403701 , 3 ,
256 , 25.566231152463722 , 3 ,
512 , 40.00811589396948 , 3 ,
1024 , 64.11373370185173 , 3 ,
2048 , 100.52011976431889 , 3 ,
4096 , 157.6689884444984 , 3 ,
8192 , 249.92825384184837 , 3 ,
16384 , 397.8033977865114 , 3 ,
"""
"""
16 , 6.528515542066423 , 4 ,
32 , 9.421539495153944 , 4 ,
64 , 16.443553523590857 , 4 ,
128 , 27.35667731012516 , 4 ,
256 , 45.73764069599367 , 4 ,
512 , 74.30827006318503 , 4 ,
1024 , 125.15709732233034 , 4 ,
2048 , 208.3152192080025 , 4 ,
4096 , 346.82834625961203 , 4 ,
8192 , 579.5092089264452 , 4 ,
16384 , 972.6004661388808 , 4,
"""

"""
time:
16 , 0.00025916099548339844 , 0 ,
32 , 0.0005280971527099609 , 0 ,
64 , 0.001519918441772461 , 0 ,
128 , 0.003036975860595703 , 0 ,
256 , 0.008514881134033203 , 0 ,
512 , 0.016628026962280273 , 0 ,
1024 , 0.04317116737365723 , 0 ,
2048 , 0.08599019050598145 , 0 ,
4096 , 0.19722890853881836 , 0 ,
"""