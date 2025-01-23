#!/usr/bin/make -f

VERSION_FILE := smartystreets_python_sdk_version/__init__.py

clean:
	rm -rf dist/ MANIFEST
	git checkout "$(VERSION_FILE)"

test: clean dependencies
	python3 -m unittest discover -p *_test.py

dependencies:
	python3 -m pip install -r requirements.txt

package: test
	echo "__version__=\"${VERSION}\"" >> "$(VERSION_FILE)" \
		&& python3 -m build

.PHONY: clean test dependencies package
