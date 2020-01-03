# Quick Python web API and PostGIS database (for testing)

Usage

```sh
docker-compose up
```
This will start the database and API with hot reload.

# FastAPI
The entrypoint to the Python app is `api/main.py`.

The example endpoint is at http://localhost:8000/api/v1/hello

FastAPI docs: https://fastapi.tiangolo.com/tutorial/first-steps/

# PostGIS

Access the `psql` client with `make psql` (see `Makefile`)

Connection strings for other database tools: `"dbname=postgres user=postgres host=localhost port=5432 password=postgres"` or `"postgres://postgres:postgres@localhost:5432/postgres"`
