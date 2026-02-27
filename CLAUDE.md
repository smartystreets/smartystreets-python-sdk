# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Build and Test Commands

```bash
# Run all tests
make test

# Run a single test file
python3 -m unittest test/us_street/client_test.py

# Run a single test method
python3 -m unittest test.us_street.client_test.TestClient.test_single_lookup_fields_set_correctly

# Install dependencies
make dependencies

# Build distribution package
make package

# Run all example scripts
make examples
```

## Architecture Overview

This is the official SmartyStreets Python SDK supporting Python 2.7 and 3.5+. It provides clients for 9 address validation/geocoding APIs.

### HTTP Pipeline Architecture

The SDK uses a **decorator pattern sender chain** for HTTP request processing. Each sender wraps the next, built inner-to-outer by `ClientBuilder.build_sender()`:

```
LicenseSender → URLPrefixSender → RetrySender → SigningSender → CustomQuerySender → CustomHeaderSender → StatusCodeSender → RequestsSender
(outermost)                                                                                                                    (innermost)
```

The chain is constructed in this exact order (see `client_builder.py:build_sender`):
1. `RequestsSender` - Makes actual HTTP calls via `requests` library
2. `StatusCodeSender` - Maps HTTP status codes to exceptions
3. `CustomHeaderSender` - Injects custom headers (if configured)
4. `CustomQuerySender` - Injects custom query params (if configured)
5. `SigningSender` - Adds authentication via `credentials.sign(request)`
6. `RetrySender` - Retries on 408/429/5xx with exponential backoff (if max_retries > 0)
7. `URLPrefixSender` - Prepends API base URL
8. `LicenseSender` - Adds license parameters (outermost)

Requests flow outer→inner: each sender's `send()` mutates the `Request` object then calls `self.inner.send()`. The `Request` object acts as a **mutable carrier** through the entire chain.

### API Module Pattern

All 9 API services follow a consistent structure under `smartystreets_python_sdk/`:
- `client.py` - Sends lookups via sender/serializer
- `lookup.py` - Input parameters for the API
- `candidate.py` / `result.py` - Response objects
- `components.py`, `metadata.py`, `analysis.py` - Supporting response types

**Two client patterns exist:**
- **Batch-based** (us_street, us_zipcode): `send_lookup()` and `send_batch()` methods. Single lookup → GET; batch → POST with JSON body.
- **Single-lookup** (most others): `send()` method only.
- **Enrichment** (us_enrichment): Multiple typed send methods (`send_property_principal_lookup`, `send_risk_lookup`, etc.) using URL path components instead of query params.

### Request Flow

1. Create `Lookup` object with input parameters
2. Add to `Batch` (optional for single lookups; max 100)
3. Call `client.send_lookup()` or `client.send_batch()`
4. Single lookup → GET with query params; Multiple → POST with JSON body
5. Results deserialized and attached back to original `Lookup.result` (matched by `input_index`)

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
