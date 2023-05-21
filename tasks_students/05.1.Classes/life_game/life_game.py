class LifeGame:
    def __init__(self, ocean):
        self.ocean = ocean
        self.rows = len(ocean)
        self.cols = len(ocean[0])

    def get_next_generation(self):
        next_ocean = [[0] * self.cols for _ in range(self.rows)]

        for i in range(self.rows):
            for j in range(self.cols):
                cell = self.ocean[i][j]
                neighbors = self.__get_neighbors(i, j)

                if cell == 0:
                    if self.__count_fish_neighbors(neighbors) == 3:
                        next_ocean[i][j] = 2
                    elif self.__count_shrimp_neighbors(neighbors) == 3:
                        next_ocean[i][j] = 3
                elif cell == 2:
                    if self.__count_fish_neighbors(neighbors) in (2, 3):
                        next_ocean[i][j] = 2
                elif cell == 3:  # shrimp
                    if self.__count_shrimp_neighbors(neighbors) in (2, 3):
                        next_ocean[i][j] = 3
                else:
                    next_ocean[i][j] = 1

        self.ocean = next_ocean
        return self.ocean

    def __get_neighbors(self, i, j):
        neighbors = []
        for x in range(max(0, i - 1), min(i + 2, self.rows)):
            for y in range(max(0, j - 1), min(j + 2, self.cols)):
                if (x, y) != (i, j):
                    neighbors.append(self.ocean[x][y])
        return neighbors

    def __count_fish_neighbors(self, neighbors):
        return neighbors.count(2)

    def __count_shrimp_neighbors(self, neighbors):
        return neighbors.count(3)
