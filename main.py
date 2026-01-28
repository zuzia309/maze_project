from __future__ import annotations

import argparse
import random
from typing import Optional, List

from maze.model import Maze, Cell
from maze.generators import generate_dfs, generate_prim
from maze.solve import random_border_cell, farthest_border_exit, solve_bfs
from maze.render_ascii import render_ascii
from maze.render_mpl import render_matplotlib


def build_maze(rows: int, cols: int, algo: str, seed: Optional[int]) -> tuple[Maze, Cell, Cell]:
    """Buduje kompletny labirynt: ustawia seed (opcjonalnie), losuje wejście na brzegu,
    generuje przejścia (DFS/Prim), a następnie wybiera wyjście jako najdalszą komórkę brzegową (BFS)."""
    if seed is not None:
        random.seed(seed)

    maze = Maze(rows, cols)

    # wejscie
    entrance_cell, entrance_side = random_border_cell(rows, cols)
    maze.open_to_outside(entrance_cell, entrance_side)

    if algo == "dfs":
        generate_dfs(maze, entrance_cell)
    elif algo == "prim":
        generate_prim(maze, entrance_cell)
    else:
        raise ValueError("Unknown algo. Use dfs or prim.")

    #wyjscie
    exit_cell, exit_side = farthest_border_exit(maze, entrance_cell)
    maze.open_to_outside(exit_cell, exit_side)

    return maze, entrance_cell, exit_cell


def parse_args() -> argparse.Namespace:
    """Parsuje argumenty z terminala używając argparse."""
    p = argparse.ArgumentParser(description="Maze generator (DFS/Prim) + ASCII + PNG + optional solving.")
    p.add_argument("--rows", type=int, default=20)
    p.add_argument("--cols", type=int, default=20)
    p.add_argument("--algo", choices=["dfs", "prim"], default="dfs")
    p.add_argument("--seed", type=int, default=None)

    p.add_argument("--ascii", action="store_true", help="Print ASCII maze")
    p.add_argument("--solve", action="store_true", help="Solve maze using BFS and show path")

    p.add_argument("--out", type=str, default=None, help="Output PNG path (e.g. maze.png)")
    p.add_argument("--show", action="store_true", help="Show matplotlib window")
    p.add_argument("--no-show", action="store_true", help="Do not show matplotlib window")
    return p.parse_args()


def main() -> None:
    args = parse_args()

    if args.no_show:
        show = False
    elif args.show:
        show = True
    else:
        show = args.out is None  # show only if not saving

    maze, entrance, exit_ = build_maze(args.rows, args.cols, args.algo, args.seed)

    path: Optional[List[Cell]] = None
    if args.solve:
        path = solve_bfs(maze, entrance, exit_)

    if args.ascii:
        print(f"Entrance: {entrance}  Exit: {exit_}  Algo: {args.algo}  Seed: {args.seed}")
        print(render_ascii(maze, path=path))

    if args.out or show:
        render_matplotlib(maze, cell_size=1.0, path=path, out=args.out, show=show)


if __name__ == "__main__":
    main()