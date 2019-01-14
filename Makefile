#!/usr/bin/make -f

VERSION      := $(shell tagit -p --dry-run)
VERSION_FILE := smartystreets_python_sdk_version/__init__.py

clean:
	rm -rf dist/ MANIFEST
	git checkout "$(VERSION_FILE)"

test:
	python -m unittest discover -p *_test.py

dependencies:
	pip install -r requirements.txt

package: clean dependencies test
	echo "__version__=\"$(VERSION)\"" >> "$(VERSION_FILE)" \
		&& python setup.py sdist \
		&& git checkout "$(VERSION_FILE)"

publish-test: clean dependencies test
	echo "__version__=\"$(VERSION)\"" >> "$(VERSION_FILE)" \
		&& python setup.py sdist upload -r pypitest \
		&& git checkout "$(VERSION_FILE)"

publish-prod: publish-test
	echo "__version__=\"$(VERSION)\"" >> "$(VERSION_FILE)" \
		&& python setup.py sdist upload -r pypi \
		&& git checkout "$(VERSION_FILE)"

release: publish-prod
	tagit -p && git push origin --tags

.PHONY: clean test dependencies package publish release
