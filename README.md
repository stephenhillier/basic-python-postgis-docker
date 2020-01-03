# Quick Python web API and PostGIS database (for testing)

Usage

```sh
docker-compose up
```


# FastAPI
The entrypoint to Python app is `api/main.py`.

The example endpoint is at http://localhost:8000/api/v1/hello

docs: https://fastapi.tiangolo.com/tutorial/first-steps/ (skip the "run with uvicorn" steps- you already ran the server with docker-compose)

# PostGIS

Access the `psql` client with `make psql` (see `Makefile`)

Connection string: `"dbname=postgres user=postgres host=localhost port=5432 password=postgres"` or `"postgres://postgres:postgres@localhost:5432/postgres"`
