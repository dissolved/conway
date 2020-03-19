from random import sample


class Life:
    def __init__(self):
        self._grid = []

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def randomize(self, size_x=40, size_y=40, population=500):
        self._grid = [[False for x in range(size_x)] for y in range(size_y)]
        max_population = size_x * size_y
        for x, y in [(num % size_x, num // size_x)for num in sample(range(0, max_population), population)]:
            self._grid[y][x] = True

    @property
    def population(self):
        return sum([sum(row) for row in self._grid])

    @property
    def size_x(self):
        return len(self._grid[0])

    @property
    def size_y(self):
        return len(self._grid)

    def load(self, filename):
        with open(filename) as f:
            self._grid = [[c == "*" for c in line.strip()] for line in f.readlines()]

    def iterate(self):
        next_grid = [[None for x in range(self.size_x)] for y in range(self.size_y)]
        for y in range(self.size_y):
            for x in range(self.size_x):
                next_grid[y][x] = neighbor_rules(self._grid[y][x], self.neighbors(x, y))
        self._grid = next_grid

    def neighbors(self, x, y):
        count = sum([sum([self.value_at(x+i, y+j) for i in [-1, 0, 1]]) for j in [-1, 0, 1]])
        return count - int(self.value_at(x, y))

    def value_at(self, x, y):
        try:
            return self._grid[y][x]
        except IndexError:
            return False


def neighbor_rules(alive, neighbors):
    if (alive and neighbors in [2, 3]) or (not alive and neighbors != 3):
        return alive
    return not alive
