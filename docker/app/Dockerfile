# Dockerfile App
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

COPY ./app /app

# Install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Install PostgreSQL client
RUN apt-get update && \
    apt-get install -y postgresql-client && \
    rm -rf /var/lib/apt/lists/*