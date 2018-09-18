#!/usr/bin/make -f

VERSION_FILE = smartystreets_python_sdk/__init__.py

clean:
	@rm -rf dist/ MANIFEST
	@git checkout "$(VERSION_FILE)"

test:
	python -m unittest discover -p *_test.py

dependencies:
	pip install -r requirements.txt

package: clean
	@echo "__version__=\"$(shell tagit -p --dry-run)\"" >> "$(VERSION_FILE)"
	python setup.py sdist
	@git checkout "$(VERSION_FILE)"

test-publish: package
	twine upload --repository-url "https://test.pypi.org/legacy/" dist/*

publish: package
	twine upload dist/*

##########################################################

workspace:
	docker-compose run sdk

release:
	docker-compose run sdk make publish && tagit -p && git push origin --tags

.PHONY: clean test dependencies package test-publish publish workspace release
