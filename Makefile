.PHONY: install serve build clean index

VENV := .venv
PY := $(VENV)/bin/python
MKDOCS := $(VENV)/bin/mkdocs

$(PY):
	python3 -m venv $(VENV)

install: $(PY)
	$(PY) -m pip install --upgrade pip
	$(PY) -m pip install -r requirements.txt

serve: install
	$(MKDOCS) serve

build: install
	$(MKDOCS) build --strict

index:
	python3 scripts/build_chapter_indexes.py

clean:
	rm -rf site
