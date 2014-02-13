PY := bin/python
PIP = bin/pip
NOSE = bin/nosetests

# ###########
# Build
# ###########

.PHONY: install
install: venv develop

venv:
	virtualenv .

$(PY): venv
$(PIP): venv

.PHONY: clean_all
clean_all: clean clean_venv

.PHONY: clean_venv
clean_venv:
	rm -rf bin include lib local

.PHONY: clean
clean:
	find . -name '*.pyc' -delete
	find . -name '*.bak' -delete
	rm -f .coverage

develop: lib/python*/site-packages/jujuplugin.egg-link
lib/python*/site-packages/jujuplugin.egg-link:
	$(PY) setup.py develop

.PHONY: sysdeps
sysdeps:
	sudo apt-get install python-dev build-essential python-virtualenv python-flake8

# ###########
# Develop
# ###########

$(NOSE): $(PY)
	$(PIP) install -r requirements.test.txt

.PHONY: test
test: $(NOSE)
	@$(NOSE) --nologcapture

.PHONY: coverage
coverage:
	@echo Testing with coverage...
	@$(NOSE) --nologcapture --with-coverage --cover-package=jujuplugin

.PHONY: lint
lint:
	@find $(sources) -type f \( -iname '*.py' ! -iname '__init__.py' ! -iwholename '*venv/*' \) -print0 | xargs -r0 flake8

.PHONY: check
check: test lint

.PHONY: all
all: clean venv coverage lint
