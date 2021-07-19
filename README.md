# Manhattan Distance with Mutation Testing

Manhattan distance is the distance between two points in a grid (like the grid-like street geography of the New York borough of Manhattan) calculated by only taking a vertical and/or horizontal path.

Write a function int manhattanDistance(Point, Point) that returns the Manhattan Distance between the two points.

# Mutation Testing with Mutmut

Install Poetry

    command -v poetry || curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

Installing mut.py into the environment

``` shell
poetry install
```

## First Experimentation

Running mutmut

``` shell
poetry run mutmut run --paths-to-mutate=manhattan.py --runner "python -m pytest"
```

and run

```
poetry run mutmut html &&  open html/index.html
```
