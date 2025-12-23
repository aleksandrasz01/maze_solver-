import pygame
import sys
from maze import Maze
from algorithms import bfs, dfs, astar
from constants import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Solver Visualizer")
clock = pygame.time.Clock()


def draw_cell(cell, color):
    pygame.draw.rect(
        screen,
        color,
        (cell.col * CELL_SIZE, cell.row * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    )
    pygame.display.update()


def draw_maze(maze):
    screen.fill(WHITE)
    for row in maze.grid:
        for cell in row:
            color = BLACK if cell.wall else WHITE
            draw_cell(cell, color)

    draw_cell(maze.start, GREEN)
    draw_cell(maze.end, RED)


def draw_step(cell, state):
    if state == "visited":
        draw_cell(cell, PURPLE)
    elif state == "frontier":
        draw_cell(cell, BLUE)
    clock.tick(60)


def draw_path(path):
    for cell in path:
        draw_cell(cell, YELLOW)
        clock.tick(30)


def main():
    maze = Maze(ROWS, COLS)
    draw_maze(maze)

    algorithm = astar  # switch to bfs / dfs

    path = algorithm(maze.start, maze.end, draw_step)
    draw_path(path)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


if __name__ == "__main__":
    main()
