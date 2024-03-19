Inf = int(1e9)

class Graph:
    def __init__(self, G: list[list[int]]) -> None:
        self.G = G
        self.n = len(G)

    def min(self, dist, visited):
        min_u = -1
        min_d = Inf
        for u, d in enumerate(dist):
            if u not in visited and d < min_d:
                min_u = u
                min_d = d
        return min_u

    def shortest_path_from(self, start: int):
        visited: set[int] = set()
        dist: list[int] = [Inf for _ in range(self.n)]
        dist[start] = 0

        while len(visited) < self.n:
            u = self.min(dist, visited)
            visited.add(u)
            for v in range(self.n):
                if self.G[u][v] != -1 and dist[v] > dist[u] + self.G[u][v]:
                    dist[v] = dist[u] + self.G[u][v]
        return dist

if __name__ == "__main__":
    g = Graph([
        # 0  1  2  3  4  5
        [-1, 2,-1,-1, 1,-1], # 0
        [ 2,-1, 1, 2, 2, 3], # 1
        [-1, 1,-1,-1, 3, 4], # 2
        [-1, 2,-1,-1, 1, 3], # 3
        [ 1, 2, 3, 1,-1,-1], # 4
        [-1, 3, 4, 3,-1,-1], # 5
    ])

    print("shortest path from 0:", g.shortest_path_from(0))
    print("shortest path from 5:", g.shortest_path_from(5))
