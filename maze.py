import random

class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.wall = True
        self.neighbors = []

    def __repr__(self):
        return f"Cell({self.row}, {self.col})"


class Maze:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[Cell(r, c) for c in range(cols)] for r in range(rows)]
        self.start = self.grid[0][0]
        self.end = self.grid[rows - 1][cols - 1]
        self.generate()

    def generate(self):
        """Recursive backtracking maze generation"""
        stack = []
        current = self.start
        current.wall = False
        stack.append(current)

        while stack:
            current = stack.pop()
            neighbors = self.get_unvisited_neighbors(current)

            if neighbors:
                stack.append(current)
                next_cell = random.choice(neighbors)
                next_cell.wall = False
                stack.append(next_cell)

        self.build_neighbors()

    def get_unvisited_neighbors(self, cell):
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        neighbors = []

        for dr, dc in directions:
            r, c = cell.row + dr, cell.col + dc
            if 0 <= r < self.rows and 0 <= c < self.cols:
                if self.grid[r][c].wall:
                    neighbors.append(self.grid[r][c])
        return neighbors

    def build_neighbors(self):
        for row in self.grid:
            for cell in row:
                if cell.wall:
                    continue
                r, c = cell.row, cell.col
                for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < self.rows and 0 <= nc < self.cols:
                        neighbor = self.grid[nr][nc]
                        if not neighbor.wall:
                            cell.neighbors.append(neighbor)
