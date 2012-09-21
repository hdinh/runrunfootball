class PlayField(object):
    def __init__(self,
                 grid=(60, 100)):
        self._grid = grid

    def grid(self, grid):
        return PlayField(grid=grid)

    def get_grid(self):
        return self._grid

    def get_yardline(self, y):
        return y *(100.0 / self._grid[1])
