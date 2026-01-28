from __future__ import annotations

from typing import List, Optional, Set

from .model import Maze, Cell


def render_ascii(maze: Maze, path: Optional[List[Cell]] = None) -> str:
    """Tworzy tekstową reprezentację labiryntu w ASCII."""
    path_set: Set[Cell] = set(path) if path else set()
    lines: List[str] = []

    # gorna sciana
    top = "+"
    for c in range(maze.cols):
        cell = (0, c)
        top += ("---" if maze.walls[cell]["top"] else "   ") + "+"
    lines.append(top)

    for r in range(maze.rows):
        # po wierszach
        line1 = ("|" if maze.walls[(r, 0)]["left"] else " ") # lewa sciana
        for c in range(maze.cols):
            cell = (r, c)
            content = " * " if cell in path_set else "   "
            line1 += content
            line1 += ("|" if maze.walls[cell]["right"] else " ")
        lines.append(line1)

        # bottom walls row
        line2 = "+"
        for c in range(maze.cols):
            cell = (r, c)
            line2 += ("---" if maze.walls[cell]["bottom"] else "   ") + "+"
        lines.append(line2)

    return "\n".join(lines) #laczymy linie w jeden string odzielony znakiem nowej lini