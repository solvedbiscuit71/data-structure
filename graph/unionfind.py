class UnionFind:
    def __init__(self, size):
        self.id = list(range(size))
        self.rank = [1] * size

    def find(self, p):
        if self.id[p] == p:
            return p
        else:
            root = self.find(self.id[p])
            self.id[p] = root
            return root

    def union(self, p1, p2):
        root1 = self.find(p1)
        root2 = self.find(p2)

        if root1 == root2:
            return False
        elif self.rank[root2] <= self.rank[root1]:
            self.rank[root1] += self.rank[root2] 
            self.id[root2] = root1
        else:
            self.rank[root2] += self.rank[root1]
            self.id[root1] = root2
        return True

    # debug purpose
    def components(self):
        d = {}
        for p in range(len(self.id)):
            root = self.find(p)
            if root in d:
                d[root].append(p)
            else:
                d[root] = [p]
        return d
