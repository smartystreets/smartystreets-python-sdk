# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Build and Test Commands

```bash
# Run all tests (installs dependencies first)
make test

# Run all tests without reinstalling dependencies (faster iteration)
make test_dev

# Run a single test file
python3 -m unittest test.us_street.client_test

# Run a single test method
python3 -m unittest test.us_street.client_test.TestClient.test_single_lookup_fields_set_correctly

# Install dependencies
make dependencies

# Build distribution package
make package
```

No linting or type-checking tools are configured in this project.

## Architecture Overview

This is the official SmartyStreets Python SDK. It provides clients for 9 address validation/geocoding APIs.

### HTTP Pipeline Architecture

The SDK uses a **decorator pattern sender chain** for HTTP request processing. Each sender wraps the next, built inner-to-outer by `ClientBuilder.build_sender()`:

```
LicenseSender → URLPrefixSender → RetrySender → SigningSender → CustomQuerySender → CustomHeaderSender → StatusCodeSender → RequestsSender
(outermost)                                                                                                                    (innermost)
```

The chain is constructed in this exact order (see `client_builder.py:build_sender`):
1. `RequestsSender` - Makes actual HTTP calls via `requests` library
2. `StatusCodeSender` - Maps HTTP status codes to exceptions
3. `CustomHeaderSender` - Injects custom headers *(only if configured)*
4. `CustomQuerySender` - Injects custom query params *(only if configured)*
5. `SigningSender` - Adds authentication via `credentials.sign(request)` *(only if credentials set)*
6. `RetrySender` - Retries on 408/429/5xx with exponential backoff *(only if max_retries > 0)*
7. `URLPrefixSender` - Prepends API base URL
8. `LicenseSender` - Adds license parameters (outermost)

Senders 3-6 are conditional — they are only added to the chain when their corresponding builder options are configured. Requests flow outer→inner: each sender's `send()` mutates the `Request` object then calls `self.inner.send()`. The `Request` object acts as a **mutable carrier** through the entire chain.

### API Module Pattern

Each API service follows a consistent structure under `smartystreets_python_sdk/`:
- `client.py` - Sends lookups via sender/serializer
- `lookup.py` - Input parameters for the API
- `candidate.py` / `result.py` - Response objects
- `components.py`, `metadata.py`, `analysis.py` - Supporting response types

**Three client patterns exist:**
- **Batch-based** (us_street, us_zipcode): `send_lookup()` and `send_batch()` methods. Batch of 1 → GET with query params; batch >1 → POST with JSON body.
- **Single-lookup** (us_extract, us_autocomplete_pro, us_reverse_geo, international_street, international_autocomplete, international_postal_code): `send()` method only, always GET.
- **Enrichment** (us_enrichment): Multiple typed send methods (`send_property_principal_lookup`, `send_geo_reference_lookup`, `send_risk_lookup`, `send_secondary_lookup`, `send_secondary_count_lookup`, `send_generic_lookup`). Uses `request.url_components` to build URL paths like `{smartykey}/{dataset}/{dataSubset}` or `search/{dataset}/{dataSubset}`.

### Request Flow

1. Create `Lookup` object with input parameters
2. Add to `Batch` (optional for batch-based APIs; max 100)
3. Call `client.send_lookup()` / `client.send_batch()` / `client.send()`
4. Results deserialized and attached back to original `Lookup.result` (matched by `input_index` for batch APIs)

### Authentication

Three credential types in `smartystreets_python_sdk/`, all implementing `sign(request)`:
- `StaticCredentials` - Server-to-server (auth_id + auth_token as query params)
- `SharedCredentials` - Client-side/embedded (API key + hostname via referer)
- `BasicAuthCredentials` - HTTP Basic Auth (sets `request.auth` tuple)

### Header Handling

Custom headers support two modes via `ClientBuilder`:
- `with_custom_header(dict)` - Multi-value headers (default, values stored as lists)
- `with_appended_header(key, value, separator)` - Single-value headers joined by separator (e.g., User-Agent)

### Testing Structure

Tests use Python's `unittest` framework, mirroring the package structure under `test/`. Mock utilities in `test/mocks/`:
- `RequestCapturingSender` - Captures sent request, returns empty 200 response
- `MockSender` - Returns predefined response
- `FakeSerializer` / `FakeDeserializer` - Capture and return preset serialization data
