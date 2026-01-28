from __future__ import annotations

import random
from collections import deque
from typing import Dict, List, Optional, Tuple

from .model import Maze, Cell

def random_border_cell(rows: int, cols: int) -> Tuple[Cell, str]:
    """Losuje komórkę na brzegu siatki oraz stronę ściany do otwarcia na zewnątrz."""
    side = random.choice(["top", "bottom", "left", "right"])
    if side == "top":
        return (0, random.randrange(cols)), "top"
    if side == "bottom":
        return (rows - 1, random.randrange(cols)), "bottom"
    if side == "left":
        return (random.randrange(rows), 0), "left"
    return (random.randrange(rows), cols - 1), "right"


def bfs_distances(maze: Maze, start: Cell) -> Dict[Cell, int]:
    """Liczy odległości BFS od komórki start do wszystkich osiągalnych komórek."""
    dist: Dict[Cell, int] = {start: 0}
    q = deque([start])
    while q:
        cur = q.popleft()
        for nb in maze.passages_neighbors(cur):
            if nb not in dist:
                dist[nb] = dist[cur] + 1
                q.append(nb)
    return dist


def farthest_border_exit(maze: Maze, entrance: Cell) -> Tuple[Cell, str]:
    """Wybiera wyjście jako najdalszą (wg BFS) komórkę na brzegu, różną od wejścia."""
    dist = bfs_distances(maze, entrance)

    border: List[Tuple[Cell, str]] = []
    for r in range(maze.rows):
        border.append(((r, 0), "left"))
        border.append(((r, maze.cols - 1), "right"))
    for c in range(maze.cols):
        border.append(((0, c), "top"))
        border.append(((maze.rows - 1, c), "bottom"))

    # remove duplicates (corners)
    seen = set()
    border_unique = []
    for item in border:
        if item not in seen:
            seen.add(item)
            border_unique.append(item)

    best: Optional[Tuple[Cell, str]] = None
    best_d = -1
    for cell, side in border_unique:
        if cell in dist and cell != entrance and dist[cell] > best_d:
            best = (cell, side)
            best_d = dist[cell]

    if best is None:
        # fallback
        for cell, side in border_unique:
            if cell != entrance:
                return cell, side
        return entrance, "top"

    return best


def solve_bfs(maze: Maze, start: Cell, goal: Cell) -> Optional[List[Cell]]:
    """Wyznacza najkrótszą ścieżkę od start do goal używając BFS."""
    q = deque([start])
    prev: Dict[Cell, Optional[Cell]] = {start: None}

    while q:
        cur = q.popleft()
        if cur == goal:
            break
        for nb in maze.passages_neighbors(cur):
            if nb not in prev:
                prev[nb] = cur
                q.append(nb)

    if goal not in prev:
        return None

    path: List[Cell] = []
    cur: Optional[Cell] = goal
    while cur is not None:
        path.append(cur)
        cur = prev[cur]
    path.reverse()
    return path