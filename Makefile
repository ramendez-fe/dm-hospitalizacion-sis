.PHONY: install ingesta dataset entrenar test lint lab clean

PY ?= python

install:
	$(PY) -m pip install -e ".[dev]"

ingesta:
	$(PY) scripts/run_ingesta.py

dataset:
	$(PY) scripts/run_build_dataset.py

entrenar:
	$(PY) scripts/run_train.py

test:
	$(PY) -m pytest -q

lint:
	ruff check src tests scripts
	ruff format --check src tests scripts

lab:
	jupyter lab

clean:
	rm -rf .pytest_cache .ruff_cache duckdb_tmp
