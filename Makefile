#!/usr/bin/make -f

SOURCE_VERSION := 3.2
VERSION_FILE = smartystreets_python_sdk/__init__.py

test: dependencies
	python -m unittest discover -p *_test.py

dependencies:
	pip install -r requirements.txt

clean:
	@rm -rf dist/ MANIFEST

package: dependencies clean
	@echo "__version__=\"$(shell git describe)\"" >> "$(VERSION_FILE)"
	python setup.py sdist
	@git checkout "$(VERSION_FILE)"

test-publish: package
	twine upload --repository-url "https://test.pypi.org/legacy/" dist/*

publish:
	twine upload dist/*

version:
	$(eval PREFIX := $(SOURCE_VERSION).)
	$(eval CURRENT := $(shell git describe 2>/dev/null))
	$(eval EXPECTED := $(PREFIX)$(shell git tag -l "$(PREFIX)*" | wc -l | xargs expr -1 +))
	$(eval INCREMENTED := $(PREFIX)$(shell git tag -l "$(PREFIX)*" | wc -l | xargs expr 0 +))
	@if [ "$(CURRENT)" != "$(EXPECTED)" ]; then git tag -a "$(INCREMENTED)" -m "" 2>/dev/null || true; fi
