from __future__ import annotations

import random
from typing import List, Tuple

from .model import Maze, Cell, DIRS, DIR_ORDER


def generate_dfs(maze: Maze, start: Cell) -> None:
    """Randomized DFS"""
    visited = [[False] * maze.cols for _ in range(maze.rows)]
    stack: List[Cell] = [start]
    visited[start[0]][start[1]] = True

    while stack:
        r, c = stack[-1]
        dirs = list(DIR_ORDER) #lista kierunkow
        random.shuffle(dirs) #mieszamy dla losowosci

        moved = False
        for d in dirs:
            dr, dc, _opp = DIRS[d]
            nr, nc = r + dr, c + dc
            if maze.in_bounds(nr, nc) and not visited[nr][nc]: # jesli sasiad jest w planszy i nie byl odwiedzony
                maze.remove_wall((r, c), d) # usuwamy sciane miedzy aktualna komorka a sasiadem (przejscie)
                visited[nr][nc] = True
                stack.append((nr, nc))
                moved = True
                break

        if not moved:
            stack.pop()


def generate_prim(maze: Maze, start: Cell) -> None:
    """Randomized Prim"""
    visited = [[False] * maze.cols for _ in range(maze.rows)]
    visited[start[0]][start[1]] = True

    frontier: List[Tuple[Cell, str, Cell]] = []

    def add_frontier(cell: Cell) -> None:
        for d, nb in maze.neighbors_cells(cell):
            r, c = nb
            if not visited[r][c]:
                frontier.append((cell, d, nb))

    add_frontier(start)

    while frontier:
        idx = random.randrange(len(frontier))
        from_cell, d, to_cell = frontier.pop(idx)

        tr, tc = to_cell
        if visited[tr][tc]:
            continue

        maze.remove_wall(from_cell, d)
        visited[tr][tc] = True
        add_frontier(to_cell)