# Repository Guidelines

## Project Overview
- Flask service that acts as a cache for Google Maps reverse geocoding responses.
- MongoDB stores cached geocoding results; Google API is called on cache misses.
- Main entrypoint is `app.py` exposing `/maps/api/geocode/status` and `/maps/api/geocode/json`.

## Repository Layout
- `app.py` — Flask routes and app object.
- `controller.py` — request validation, cache lookup, Google API fallback, cache storage.
- `database.py` — MongoDB connection and cache operations.
- `apis.py` — Google Geocoding API client.
- `config.py` — environment-backed configuration defaults.
- `validations.py` — request parameter validation helpers.
- `requirements.txt` — Python runtime dependencies.
- `Dockerfile` — container image definition.

## Local Development
```bash
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
gunicorn app:app
```

Run MongoDB locally when exercising cache behavior:
```bash
docker run --name mongo -d mongo:latest
```

Health check endpoint:
```bash
curl http://localhost:8000/maps/api/geocode/status
```

## Testing and Checks
- No test suite is currently present.
- For syntax checks, run:
```bash
python3 -m py_compile *.py
```
- When changing behavior, prefer adding focused tests before broad refactors.

## Coding Guidelines
- Keep changes small and consistent with the existing simple module structure.
- Do not commit secrets or real API keys; use environment variables for credentials/configuration.
- Be careful with external Google API calls in tests; mock `requests.get` where possible.
- Preserve public route behavior unless explicitly asked to change it.
