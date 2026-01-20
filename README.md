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
	- Wejście: losowane na brzegu labiryntu (góra/dół/lewo/prawo)
	- Wyjście: wybierane jako najdalsza osiągalna komórka na brzegu (na podstawie BFS), dzięki czemu zwykle daje dłuższą i ciekawszą trasę.

⸻ ⸻ ⸻ ⸻ ⸻ ⸻ ⸻ ⸻ ⸻ ⸻ ⸻ ⸻ ⸻ ⸻ ⸻


## Algorytmy

Randomized DFS (recursive backtracker)

Start z komórki wejściowej → losowo wybierany nieodwiedzony sąsiad → usunięcie ściany → przejście dalej.
Gdy brak ruchu, cofanie po stosie.
Efekt: często dłuższe korytarze.

Randomized Prim

Utrzymywana jest lista “krawędzi granicznych” z już dołączonych komórek do nieodwiedzonych.
Losowo wybierana krawędź → dołączenie nowej komórki i usunięcie ściany.
Efekt: więcej rozgałęzień, bardziej “poszarpany” styl labiryntu.

BFS (rozwiązywanie)

Labirynt traktowany jako graf nieważony: komórki = wierzchołki, przejścia = krawędzie.
BFS zwraca najkrótszą ścieżkę od wejścia do wyjścia.

⸻ ⸻ ⸻ ⸻ ⸻ ⸻ ⸻ ⸻ ⸻ ⸻ ⸻ ⸻ ⸻ ⸻ ⸻

Autor

Zuzanna Czerwińska













