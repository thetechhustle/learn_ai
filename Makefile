.PHONY: install serve build clean index audit audit-test

VENV := .venv
PY := $(VENV)/bin/python
MKDOCS := $(VENV)/bin/mkdocs
DEPS := $(VENV)/.requirements.stamp

$(PY):
	python3 -m venv $(VENV)

$(DEPS): requirements.txt $(PY)
	$(PY) -m pip install --upgrade pip
	$(PY) -m pip install -r requirements.txt
	touch $(DEPS)

install: $(DEPS)

serve: install
	$(MKDOCS) serve

build: install
	$(MKDOCS) build --strict

index:
	python3 scripts/build_chapter_indexes.py

audit:
	python3 scripts/audit_course.py

audit-test:
	python3 scripts/audit_course.py --self-test

clean:
	rm -rf site
