from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable, List, Tuple

Cell = Tuple[int, int]  # (row, col)

DIRS = {
    "top":    (-1, 0, "bottom"),
    "right":  (0, 1, "left"),
    "bottom": (1, 0, "top"),
    "left":   (0, -1, "right"),
}
DIR_ORDER = ("top", "right", "bottom", "left")


@dataclass
class Maze:
    rows: int
    cols: int

    def __post_init__(self) -> None:
        if self.rows <= 0 or self.cols <= 0:
            raise ValueError("rows and cols must be > 0")

        self.walls: Dict[Cell, Dict[str, bool]] = {
            (r, c): {"top": True, "right": True, "bottom": True, "left": True}
            for r in range(self.rows)
            for c in range(self.cols)
        }

    def in_bounds(self, r: int, c: int) -> bool:
        return 0 <= r < self.rows and 0 <= c < self.cols

    def neighbors_cells(self, cell: Cell) -> Iterable[Tuple[str, Cell]]:
        r, c = cell
        for d in DIR_ORDER:
            dr, dc, _opp = DIRS[d]
            nr, nc = r + dr, c + dc
            if self.in_bounds(nr, nc):
                yield d, (nr, nc)

    def remove_wall(self, a: Cell, dir_name: str) -> None:
        r, c = a
        dr, dc, opposite = DIRS[dir_name]
        b = (r + dr, c + dc)
        if not self.in_bounds(*b):
            return
        self.walls[a][dir_name] = False
        self.walls[b][opposite] = False

    def open_to_outside(self, cell: Cell, side: str) -> None:
        r, c = cell
        if side == "top" and r == 0:
            self.walls[cell]["top"] = False
        elif side == "bottom" and r == self.rows - 1:
            self.walls[cell]["bottom"] = False
        elif side == "left" and c == 0:
            self.walls[cell]["left"] = False
        elif side == "right" and c == self.cols - 1:
            self.walls[cell]["right"] = False

    def passages_neighbors(self, cell: Cell) -> List[Cell]:
        r, c = cell
        out: List[Cell] = []
        for d, (nr, nc) in self.neighbors_cells(cell):
            if self.walls[(r, c)][d] is False:
                out.append((nr, nc))
        return out