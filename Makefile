.PHONY: help setup test dash

help:
	@echo "Available targets:"
	@echo "  setup   - create venv, install dev deps"
	@echo "  test    - run pytest"
	@echo "  dash    - run the example dashboard script"

setup:
	python3 -m venv .venv && . .venv/bin/activate && pip install -U pip && pip install -r requirements-dev.txt

test:
	pytest -q

dash:
	python tools/hello_core.py
