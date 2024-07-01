class IndexedHeap:
    """
    Convension: i, j are node index and ki, kj are key index
    """
    def __init__(self, N):
        self.N = N
        self.size = 0

        self.values = [None] * N     # key index => value
        self.pm = [None] * N        # position map: key index => node index
        self.im = [None] * N        # inverse map: node index => key index

    def less(self, i, j):
        return self.values[self.im[i]] < self.values[self.im[j]]

    def swap(self, i, j):
        ki = self.im[i]
        kj = self.im[j]
        self.im[i] = kj
        self.im[j] = ki
        self.pm[ki] = j
        self.pm[kj] = i

    def swin(self, i):
        p = (i-1) // 2
        while p >= 0:
            if self.less(p, i):
                break
            self.swap(i, p)
            i = p
            p = (i-1) // 2

    def sink(self, i):
        left = 2*i + 1
        right = 2*i + 2
        minimum = right if right < self.size and self.less(right, left) else left

        while minimum < self.size:
            if self.less(i, minimum):
                break
            self.swap(i, minimum)

            i = minimum
            left = 2*i + 1
            right = 2*i + 2
            minimum = right if right < self.size and self.less(right, left) else left

    def insert(self, ki, value):
        i = self.size
        self.values[ki] = value
        self.im[i] = ki
        self.pm[ki] = i
        self.size += 1
        self.swin(i)

    def remove(self, ki):
        i = self.pm[ki]
        j = self.size - 1
        self.swap(i, j)

        self.values[ki] = None
        self.pm[ki] = None
        self.im[j] = None 
        self.size -= 1

        self.swin(i)
        self.sink(i)


    def update(self, ki, value):
        self.values[ki] = value
        i = self.pm[ki]
        self.swin(i)
        self.sink(i)

    def decreaseKey(self, ki, value):
        if value < self.values[ki]:
            self.values[ki] = value
            self.swin(self.pm[ki])

    def increaseKey(self, ki, value):
        if value > self.values[ki]:
            self.values[ki] = value
            self.sink(self.pm[ki])

    def poll(self):
        if self.size == 0:
            return None
        return (self.im[0], self.values[self.im[0]])

    def pop(self):
        if self.size == 0:
            return None
        key, value = self.poll()
        self.remove(key)
        return key, value
