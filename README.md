# Maze Generator (DFS / Randomized Prim) — Python

Projekt generuje labirynt na siatce `rows × cols` jako **drzewo rozpinające** grafu kratowego (*perfect maze*: brak cykli, dokładnie jedna ścieżka między każdą parą komórek).  
Obsługiwane algorytmy generowania:
- **Randomized DFS** (recursive backtracker)
- **Randomized Prim**

Labirynt można:
- wypisać w terminalu (ASCII),
- narysować / zapisać do PNG (matplotlib),
- opcjonalnie **rozwiązać** (BFS) i narysować najkrótszą ścieżkę.

⸻ ⸻ ⸻ ⸻ ⸻ ⸻ ⸻ ⸻ ⸻ ⸻ ⸻ ⸻ ⸻ ⸻ ⸻

## Struktura projektu
maze_project/
	main.py
	maze/
	   init.py
	   model.py
	   generators.py
	   solve.py
	   render_ascii.py
	   render_mpl.py

- `maze/model.py` – model labiryntu (komórki, ściany, sąsiedzi, przejścia)
- `maze/generators.py` – algorytmy generowania (DFS, Prim)
- `maze/solve.py` – wybór wejścia/wyjścia + BFS (dystanse i rozwiązanie)
- `maze/render_ascii.py` – render ASCII
- `maze/render_mpl.py` – render matplotlib (okno/PNG)
- `main.py` – CLI i uruchomienie programu

⸻ ⸻ ⸻ ⸻ ⸻ ⸻ ⸻ ⸻ ⸻ ⸻ ⸻ ⸻ ⸻ ⸻ ⸻

## Najważniejsze funkcje

Poniżej krótka lista funkcji, z których korzysta program – **co robią i gdzie są używane**.

### Budowanie labiryntu (main.py)
- `parse_args()` – wczytuje argumenty z terminala (`--rows`, `--cols`, `--algo`, itd.).
- `build_maze(rows, cols, algo, seed)` – tworzy labirynt krok po kroku: wejście -> generowanie -> wyjście.
- `main()` – uruchamia cały program: opcjonalnie rozwiązuje i renderuje.

### Model labiryntu (maze/model.py)
- `Maze.__post_init__()` – tworzy strukturę `walls` i ustawia wszystkie ściany na `True`.
- `Maze.in_bounds(r, c)` – sprawdza czy komórka mieści się w planszy.
- `Maze.neighbors_cells(cell)` – zwraca sąsiadów komórki (top/right/bottom/left).
- `Maze.remove_wall(cell, dir)` – usuwa ścianę między komórkami (tworzy przejście) i pilnuje spójności po obu stronach.
- `Maze.open_to_outside(cell, side)` – otwiera wejście/wyjście na brzegu (ustawia ścianę na `False`).
- `Maze.passages_neighbors(cell)` – zwraca tylko tych sąsiadów, do których da się przejść (brak ściany).

### Generowanie (maze/generators.py)
- `generate_dfs(maze, start)` – Randomized DFS (stos + cofanie); usuwa ściany w `maze.walls`.
- `generate_prim(maze, start)` – Randomized Prim (frontier); usuwa ściany w `maze.walls`.

### Wejście/wyjście i rozwiązywanie (maze/solve.py)
- `random_border_cell(rows, cols)` – losuje wejście na brzegu (zwraca komórkę + stronę ściany).
- `bfs_distances(maze, start)` – BFS liczący odległości od startu do wszystkich komórek.
- `farthest_border_exit(maze, entrance)` – wybiera wyjście jako najdalszą komórkę brzegową wg BFS.
- `solve_bfs(maze, start, goal)` – BFS zwracający najkrótszą ścieżkę jako listę komórek.

### Renderowanie (maze/render_ascii.py, maze/render_mpl.py)
- `render_ascii(maze, path=None)` – tworzy ASCII na podstawie `maze.walls`, opcjonalnie zaznacza ścieżkę `*`.
- `render_matplotlib(maze, cell_size=1.0, path=None, out=None, show=True)` – rysuje ściany jako odcinki (`ax.plot`), opcjonalnie rysuje ścieżkę i zapisuje PNG.
**Jak działa `ax.plot` (w skrócie):**  
W `render_matplotlib` tworzymy „płótno” Matplotlib:

- `fig, ax = plt.subplots(figsize=(8, 8))`  
  `ax` to obszar rysowania (na nim rysujemy).

Następnie każdą ścianę rysujemy jako **jeden odcinek**:
- `ax.plot([x1, x2], [y1, y2])` rysuje linię między dwoma punktami `(x1, y1)` i `(x2, y2)`.  
Dzięki temu labirynt powstaje z wielu krótkich linii (top/right/bottom/left) dla każdej komórki.
## Wymagania

- Python 3.9+
- `matplotlib` (tylko do rysowania PNG/okna; ASCII działa bez tego)


⸻ ⸻ ⸻ ⸻ ⸻ ⸻ ⸻ ⸻ ⸻ ⸻ ⸻ ⸻ ⸻ ⸻ ⸻

## Uruchomienie

1) ASCII w terminalu (bez matplotlib)

python main.py --rows 15 --cols 30 --algo dfs --ascii --no-show

2) Zapis do PNG (bez okna)

python main.py --rows 30 --cols 30 --algo prim --seed 123 --out maze.png --no-show

3) Rozwiązanie labiryntu i zapis PNG ze ścieżką 

python main.py --rows 25 --cols 25 --algo dfs --seed 7 --solve --out solved.png --no-show

4) Wyświetlenie w oknie (matplotlib)

python main.py --rows 20 --cols 20 --algo dfs --show

Parametry CLI

	--rows – liczba wierszy siatki (liczba komórek w pionie)
	--cols – liczba kolumn siatki (liczba komórek w poziomie)
	--algo – algorytm generowania: dfs lub prim
	--seed – ziarno losowości (powtarzalne wyniki)
	--ascii – wypisz labirynt w ASCII do terminala
	--solve – rozwiąż labirynt BFS i zaznacz najkrótszą ścieżkę
	--out – zapisz obraz do PNG (np. maze.png)
	--show – pokaż okno matplotlib
	--no-show – nie pokazuj okna (przydatne przy zapisie PNG)

⸻ ⸻ ⸻ ⸻ ⸻ ⸻ ⸻ ⸻ ⸻ ⸻ ⸻ ⸻ ⸻ ⸻ ⸻

## Wejście i wyjście
Wejście: losowane na brzegu labiryntu (góra/dół/lewo/prawo)

Wyjście: wybierane jako najdalsza osiągalna komórka na brzegu (na podstawie BFS), dzięki czemu zwykle daje dłuższą i ciekawszą trasę.

⸻ ⸻ ⸻ ⸻ ⸻ ⸻ ⸻ ⸻ ⸻ ⸻ ⸻ ⸻ ⸻ ⸻ ⸻


## Algorytmy

Randomized DFS (recursive backtracker)

Start z komórki wejściowej -> losowo wybierany nieodwiedzony sąsiad -> usunięcie ściany -> przejście dalej.
Gdy brak ruchu, cofanie po stosie.
Efekt: często dłuższe korytarze.

Randomized Prim

Utrzymywana jest lista “krawędzi granicznych” z już dołączonych komórek do nieodwiedzonych.
Losowo wybierana krawędź -> dołączenie nowej komórki i usunięcie ściany.
Efekt: więcej rozgałęzień, bardziej “poszarpany” styl labiryntu.

BFS (rozwiązywanie)

Labirynt traktowany jako graf nieważony: komórki = wierzchołki, przejścia = krawędzie.
BFS zwraca najkrótszą ścieżkę od wejścia do wyjścia.

⸻ ⸻ ⸻ ⸻ ⸻ ⸻ ⸻ ⸻ ⸻ ⸻ ⸻ ⸻ ⸻ ⸻ ⸻

Autor

Zuzanna Czerwińska











