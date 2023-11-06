SHELL=bash
VENV = .venv

$(VENV):
	python3 -m venv $(VENV)
	$(MAKE) install

install: $(VENV)
	$(VENV)/bin/pip install --upgrade pip setuptools wheel build
	$(VENV)/bin/pip install --editable .[dev]

format: $(VENV)
	$(VENV)/bin/black .
	$(VENV)/bin/isort .

lint: $(VENV) format
	$(VENV)/bin/pylint --output-format=colorized batchalier tests
	$(VENV)/bin/mypy batchalier tests

test: $(VENV)
	$(VENV)/bin/pytest -v tests

build: $(VENV)
	$(VENV)/bin/python -m build .

clean:
	rm -rf $(VENV) dist

.PHONY: install clean format lint test
