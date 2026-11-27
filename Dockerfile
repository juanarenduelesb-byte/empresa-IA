FROM python:3.12-slim
WORKDIR /app
COPY pyproject.toml ./
COPY src ./src
COPY migrations ./migrations
COPY alembic.ini ./
# processes: definiciones y casos inventados de la semilla (A5); tools/org_data: registro de fuentes de la semilla.
COPY processes ./processes
COPY tools/org_data ./tools/org_data
COPY oficina ./oficina
RUN pip install --no-cache-dir .
EXPOSE 8000
CMD ["sh", "-c", "alembic upgrade head && uvicorn varios.api.app:app --host 0.0.0.0 --port 8000"]
