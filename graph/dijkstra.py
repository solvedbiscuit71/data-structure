class IndexedMinHeap:
    def __init__(self, maxindex) -> None:
        self.maxindex = maxindex  # index belongs to [0, maxindex]
        self.size = 0
        self.tree: any = [None for _ in range(maxindex + 1)]  # heap stores index # type: ignore
        self.loc: any = [None for _ in range(maxindex + 1)]  # location of a particular index in the heap # type: ignore
        self.key: any = [None for _ in range(maxindex + 1)]  # index-key table # type: ignore

    def child(self, i):
        l = 2*i + 1 if 2*i + 1 < self.size else None
        r = 2*i + 2 if 2*i + 2 < self.size else None
        return l, r

    def min_child(self, i):
        l, r = self.child(i)
        if l and r:
            return r if self.key[self.tree[r]] < self.key[self.tree[l]] else l
        return l

    def parent(self, i):
        return (i-1) // 2 if i > 0 else None

    def bubble_up(self, i):
        j = self.parent(i)
        while j is not None:
            if self.key[self.tree[j]] > self.key[self.tree[i]]:
                self.tree[i], self.tree[j] = self.tree[j], self.tree[i]
                self.loc[self.tree[i]], self.loc[self.tree[j]] = self.loc[self.tree[i]], self.loc[self.tree[j]]
                i = j
                j = self.parent(i)
            else:
                break

    def bubble_down(self, i):
        j = self.min_child(i)
        while j is not None:
            if self.key[self.tree[i]] > self.key[self.tree[j]]:
                self.tree[i], self.tree[j] = self.tree[j], self.tree[i]
                self.loc[self.tree[i]], self.loc[self.tree[j]] = self.loc[self.tree[i]], self.loc[self.tree[j]]
                i = j
                j = self.min_child(i)
            else:
                break

    def push(self, i, key):
        if not (0 <= i <= self.maxindex):
            raise Exception("Index exceeds maxindex")

        if self.loc[i] is not None:
            self.setKey(i, key)
            return

        self.tree[self.size] = i
        self.loc[i] = self.size
        self.key[i] = key
        self.size += 1
        self.bubble_up(self.size - 1)

    def pop(self):
        if self.size == 0:
            return (None, None)

        i = self.tree[0]
        key = self.key[i]
        self.key[i] = None
        self.loc[i] = None # type: ignore

        self.tree[0] = self.tree[self.size - 1]
        self.loc[self.tree[self.size - 1]] = 0
        self.tree[self.size - 1] = None # type: ignore

        self.size -= 1
        if self.size > 0:
            self.bubble_down(0)
        return (i, key)

    def setKey(self, i, key):
        if self.key[i] is None:
            raise Exception("Index doesn't exist")

        old_key = self.key[i]
        self.key[i] = key
        if key > old_key:
            self.bubble_down(self.loc[i])
        elif key < old_key:
            self.bubble_up(self.loc[i])

    def getKey(self, i):
        if self.key[i] is None:
            raise Exception("Index doesn't exist")
        return self.key[i]

    def top(self):
        return (self.tree[0], self.key[self.tree[0]]) if self.tree else None

    def __len__(self):
        return self.size

    def __contains__(self, i):
        return self.loc[i] is not None

Inf = int(1e9)

class Graph:
    def __init__(self, G) -> None:
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

    def dijkstra(self, start: int, end: int):
        visited = set()
        pq = IndexedMinHeap(self.n - 1)
        pq.push(start, 0)

        while pq:
            u, d = pq.pop()
            visited.add(u)
            if u == end:
                return d
            for v in range(self.n):
                if self.G[u][v] != -1 and v not in visited and (v not in pq or d + self.G[u][v] < pq.getKey(v)):
                    pq.push(v, d + self.G[u][v])
        return Inf


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

    print("shortest path from 0-2:", g.dijkstra(0, 2))
