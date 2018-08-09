#!/usr/bin/make -f

VERSION_FILE = smartystreets_python_sdk/__init__.py

tests:
	python -m unittest discover -p *_test.py

dependencies:
	pip install -r requirements.txt

clean:
	@rm -rf dist/ MANIFEST
	@git checkout "$(VERSION_FILE)"

package: clean
	@echo "__version__=\"$(shell git describe)\"" >> "$(VERSION_FILE)"
	python setup.py sdist
	@git checkout "$(VERSION_FILE)"

test-publish: package
	twine upload --repository-url "https://test.pypi.org/legacy/" dist/*

publish: package
	twine upload dist/*

version:
	@tagit -p

####################################################################3

container-test:
	docker-compose run sdk make tests
container-package:
	docker-compose run sdk make package
container-test-publish: version
	docker-compose run sdk make test-publish
	git push origin --tags
container-publish: version
	docker-compose run sdk make publish
	git push origin --tags
