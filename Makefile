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
		&& python3 setup.py sdist

international_autocomplete_api:
	PYTHONPATH=. python3 examples/international_autocomplete_example.py

international_street_api:
	PYTHONPATH=. python3 examples/international_example.py

us_autocomplete_pro_api:
	PYTHONPATH=. python3 examples/us_autocomplete_pro_example.py

us_enrichment_api:
	PYTHONPATH=. python3 examples/us_enrichment_example.py

us_extract_api:
	PYTHONPATH=. python3 examples/us_extract_example.py

us_reverse_geo_api:
	PYTHONPATH=. python3 examples/us_reverse_geo_example.py

us_street_api:
	PYTHONPATH=. python3 examples/us_street_single_address_example.py && PYTHONPATH=. python3 examples/us_street_multiple_addresses_example.py

us_zipcode_api:
	PYTHONPATH=. python3 examples/us_zipcode_single_lookup_example.py && PYTHONPATH=. python3 examples/us_zipcode_multiple_lookups_example.py

examples: international_autocomplete_api international_street_api us_autocomplete_pro_api us_enrichment_api us_extract_api us_reverse_geo_api us_street_api us_zipcode_api


.PHONY: clean test dependencies package examples international_autocomplete_api international_street_api us_autocomplete_pro_api us_enrichment_api us_extract_api us_reverse_geo_api us_street_api us_zipcode_api
