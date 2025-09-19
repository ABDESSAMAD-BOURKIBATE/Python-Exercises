import time

# Class Cell

class Cell:
    def __init__(self, alive=False):
        self.alive = alive

    def __repr__(self):
        return "⬛" if self.alive else "⬜"


# Class Grid

class Grid:
    def __init__(self, rows, cols, initial_state=None):
        self.rows = rows
        self.cols = cols
        self.grid = [[Cell(False) for _ in range(cols)] for _ in range(rows)]

        if initial_state:
            for r, c in initial_state:
                if 0 <= r < rows and 0 <= c < cols:
                    self.grid[r][c].alive = True

    def display(self):
        for row in self.grid:
            print(" ".join(str(cell) for cell in row))
        print("\n")

    def count_neighbors(self, row, col):
        directions = [(-1,-1), (-1,0), (-1,1),
                      (0,-1),         (0,1),
                      (1,-1), (1,0),  (1,1)]
        count = 0
        for dr, dc in directions:
            r, c = row+dr, col+dc
            if 0 <= r < self.rows and 0 <= c < self.cols:
                if self.grid[r][c].alive:
                    count += 1
        return count

    def next_generation(self):
        new_grid = [[Cell() for _ in range(self.cols)] for _ in range(self.rows)]

        for r in range(self.rows):
            for c in range(self.cols):
                neighbors = self.count_neighbors(r, c)
                if self.grid[r][c].alive:
                    if neighbors == 2 or neighbors == 3:
                        new_grid[r][c].alive = True
                else:
                    if neighbors == 3:
                        new_grid[r][c].alive = True

        self.grid = new_grid


# Class Game

class Game:
    def __init__(self, grid, generations=5, delay=1):
        self.grid = grid
        self.generations = generations
        self.delay = delay

    def run(self):
        for gen in range(self.generations):
            print(f"Generation {gen+1}")
            self.grid.display()
            self.grid.next_generation()
            time.sleep(self.delay)


# Main Test

if __name__ == "__main__":

    initial_state = [(1,2), (2,3), (3,1), (3,2), (3,3)]

    grid = Grid(10, 10, initial_state)
    game = Game(grid, generations=10, delay=0.5)
    game.run()
