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

The SDK uses a **decorator pattern sender chain** for HTTP request processing:

```
ClientBuilder → API Client → Batch/Lookup → Sender Chain → HTTP
```

The sender chain processes requests in order:
1. `URLPrefixSender` - Prepends API base URL
2. `LicenseSender` - Adds license parameters
3. `RetrySender` - Handles retry logic
4. `SigningSender` - Adds authentication
5. `CustomQuerySender` / `CustomHeaderSender` - Injects custom params/headers
6. `StatusCodeSender` - Validates response codes, raises exceptions
7. `RequestsSender` - Actual HTTP via `requests` library

**Order matters** - the ClientBuilder constructs this chain in a specific sequence.

### API Module Pattern

All 9 API services follow an identical structure under `smartystreets_python_sdk/`:
- `client.py` - Sends lookups via sender/serializer
- `lookup.py` - Input parameters for the API
- `candidate.py` / `result.py` - Response objects
- `components.py`, `metadata.py`, `analysis.py` - Supporting response types

### Request Flow

1. Create `Lookup` object with input parameters
2. Add to `Batch` (optional for single lookups)
3. Call `client.send_lookup()` or `client.send_batch()`
4. Single lookup → GET with query params; Multiple → POST with JSON body
5. Results deserialized and attached back to original `Lookup.result`

### Authentication

Two credential types in `smartystreets_python_sdk/`:
- `StaticCredentials` - Server-to-server (auth_id + auth_token)
- `SharedCredentials` - Client-side/embedded (API key + hostname)

### Testing Structure

Tests use Python's `unittest` framework, mirroring the package structure under `test/`. Mock utilities in `test/mocks/` include `RequestCapturingSender` for asserting HTTP request parameters and `MockSender` for canned responses.
