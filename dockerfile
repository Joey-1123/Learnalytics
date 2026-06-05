# Base image
FROM python:3.12-slim

# Prevents python buffering logs
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy dependency files
COPY pyproject.toml uv.lock ./

# Install dependencies
RUN uv sync --no-dev --frozen

# Copy project
COPY . .

# Collect static files
RUN uv run python manage.py collectstatic --noinput

# Run server
CMD ["uv", "run", "gunicorn", "learnalytics.wsgi:application", "--bind", "0.0.0.0:8000"]