from __future__ import annotations

from typing import List, Optional

from .model import Maze, Cell


def render_matplotlib(
    maze: Maze,
    cell_size: float = 1.0,
    path: Optional[List[Cell]] = None,
    out: Optional[str] = None,
    show: bool = True,
) -> None:
    import matplotlib.pyplot as plt  # plt do tworzenia rysunkow
    """Renderuje labirynt graficznie przy użyciu biblioteki Matplotlib."""

    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_aspect("equal") # jednostka w x = jednostce y
    ax.axis("off") # ukrywamy osie

    for r in range(maze.rows):
        for c in range(maze.cols):
            x = c * cell_size #x rosnie w prawo od 0
            y = (maze.rows - r - 1) * cell_size # y jest odwrocone zeby wiersz r = 0 byl u gory
            cell = (r, c)
            w = maze.walls[cell] # slownik scian tej komorki

            if w["top"]:
                ax.plot([x, x + cell_size], [y + cell_size, y + cell_size], color="black")
            if w["right"]:
                ax.plot([x + cell_size, x + cell_size], [y, y + cell_size], color="black")
            if w["bottom"]:
                ax.plot([x, x + cell_size], [y, y], color="black")
            if w["left"]:
                ax.plot([x, x], [y, y + cell_size], color="black")

    if path and len(path) >= 2:
        xs, ys = [], []
        for (r, c) in path:
            xs.append(c * cell_size + cell_size / 2)
            ys.append((maze.rows - r - 1) * cell_size + cell_size / 2)
        ax.plot(xs, ys, linewidth=2)  # default color

    plt.tight_layout()
    if out:
        fig.savefig(out, dpi=200)
    if show:
        plt.show()
    plt.close(fig)