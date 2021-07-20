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
poetry run mutmut run --paths-to-mutate=banking.py --runner "python -m pytest"
```

and run

```
poetry run mutmut html &&  open html/index.html
```
