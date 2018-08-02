#!/usr/bin/make -f
#!/usr/bin/make -f

SOURCE_VERSION := 3.2

test: dependencies
	python -m unittest discover -p *_test.py

dependencies:
	pip install -r requirements.txt

clean:
	@rm -rf dist/
	git checkout smartystreets_python_sdk/__init__.py
	git checkout setup.py

package: clean
	python setup.py sdist

test-publish: package
	twine upload --repository-url "https://test.pypi.org/legacy/" dist/*

publish:
	twine upload dist/*

# version: tag
# 	@sed -i -r "s/0\.0\.0/$(shell git describe)/g" smartystreets_python_sdk/__init__.py
# 	@sed -i -r "s/0\.0\.0/$(shell git describe)/g" setup.py

# tag:
# 	$(eval PREFIX := $(SOURCE_VERSION).)
# 	$(eval CURRENT := $(shell git describe 2>/dev/null))
# 	$(eval EXPECTED := $(PREFIX)$(shell git tag -l "$(PREFIX)*" | wc -l | xargs expr -1 +))
# 	$(eval INCREMENTED := $(PREFIX)$(shell git tag -l "$(PREFIX)*" | wc -l | xargs expr 0 +))
# 	@if [ "$(CURRENT)" != "$(EXPECTED)" ]; then git tag -a "$(INCREMENTED)" -m "" 2>/dev/null || true; fi
