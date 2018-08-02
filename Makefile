#!/usr/bin/make -f
#!/usr/bin/make -f

SOURCE_VERSION := 3.2

test: dependencies
	python -m unittest discover -p *_test.py

dependencies:
	pip install -r requirements.txt

test-publish: 
	git push origin --tags
	python setup.py sdist upload -r pypitest
	git checkout smartystreets_python_sdk/__init__.py
	git checkout setup.py
publish:
	git push origin --tags
	python setup.py sdist upload -r pypi
	git checkout smartystreets_python_sdk/__init__.py
	git checkout setup.py

version: tag
	@sed -i -r "s/0\.0\.0/$(shell git describe)/g" smartystreets_python_sdk/__init__.py
	@sed -i -r "s/0\.0\.0/$(shell git describe)/g" setup.py

tag:
	$(eval PREFIX := $(SOURCE_VERSION).)
	$(eval CURRENT := $(shell git describe 2>/dev/null))
	$(eval EXPECTED := $(PREFIX)$(shell git tag -l "$(PREFIX)*" | wc -l | xargs expr -1 +))
	$(eval INCREMENTED := $(PREFIX)$(shell git tag -l "$(PREFIX)*" | wc -l | xargs expr 0 +))
	@if [ "$(CURRENT)" != "$(EXPECTED)" ]; then git tag -a "$(INCREMENTED)" -m "" 2>/dev/null || true; fi
