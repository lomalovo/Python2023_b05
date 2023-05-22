import typing as tp


class LifeGame:
    def __init__(self: tp.Any, ocean: tp.Any) -> None:
        self.ocean: tp.Any = ocean
        self.rows: tp.Any = len(ocean)
        self.cols: tp.Any = len(ocean[0])

    def get_next_generation(self: tp.Any) -> tp.Any:
        next_ocean: tp.Any = [[0] * self.cols for _ in range(self.rows)]

        for i in range(self.rows):
            for j in range(self.cols):
                cell: tp.Any = self.ocean[i][j]
                neighbors: tp.Any = self.__get_neighbors(i, j)

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

    def __get_neighbors(self: tp.Any, i: tp.Any, j: tp.Any) -> tp.Any:
        neighbors: tp.Any = []
        for x in range(max(0, i - 1), min(i + 2, self.rows)):
            for y in range(max(0, j - 1), min(j + 2, self.cols)):
                if (x, y) != (i, j):
                    neighbors.append(self.ocean[x][y])
        return neighbors

    def __count_fish_neighbors(self: tp.Any, neighbors: tp.Any) -> tp.Any:
        return neighbors.count(2)

    def __count_shrimp_neighbors(self: tp.Any, neighbors: tp.Any) -> tp.Any:
        return neighbors.count(3)
