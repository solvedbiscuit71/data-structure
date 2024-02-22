from math import ceil, sqrt
from dataclasses import dataclass
from typing import Any

@dataclass
class Slot:
    value: 'Any' = None
    deleted: bool = False

    def reset(self):
        self.value = None
        self.deleted = True

    def set(self, value):
        self.value = value
        self.deleted = False

    def __bool__(self):
        return self.value is not None

class HashTable:
    def __init__(self, size=8) -> None:
        self.table = [Slot() for _ in range(size)]
        self.count = 0

    def h(self, x):
        return (2 * x + 1) % len(self.table)

    def insert(self, x):
        if self.search(x):
            return

        h = self.h(x)
        for i in range(ceil(sqrt(len(self.table)))):
            # if empty slot (maybe deleted or not)
            idx = (h + i ** 2) % len(self.table)
            if not self.table[idx]:
                self.table[idx].set(x)
                break
        self.count += 1

    def remove(self, x):
        h = self.h(x)
        for i in range(ceil(sqrt(len(self.table)))):
            # if empty slot (not deleted)
            idx = (h + i ** 2) % len(self.table)
            if not self.table[idx] and not self.table[idx].deleted:
                break

            # if correct slot
            elif self.table[idx].value == x:
                self.table[idx].reset()
                break

    def search(self, x):
        h = self.h(x)
        for i in range(ceil(sqrt(len(self.table)))):
            # if empty slot (not deleted)
            idx = (h + i ** 2) % len(self.table)
            if not self.table[idx] and not self.table[idx].deleted:
                break

            # if correct slot
            elif self.table[idx].value == x:
                return True
        return False

    def __str__(self):
        x = map(lambda s: s.value if s.value is not None else None, self.table)
        return str(list(x))

    def __repr__(self) -> str:
        return self.__str__()

    def __len__(self):
        return self.count

if __name__ == "__main__":
    t = HashTable(10)
    for x in range(5, 25, 5):
        t.insert(x)
    print(t)
    t.insert(25)
    print('Inserted 25')
    print(t)
