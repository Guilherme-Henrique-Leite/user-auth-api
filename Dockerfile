FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y gcc libffi-dev

RUN pip install --upgrade pip && \
    pip install uv && \
    uv venv .venv && \
    . .venv/bin/activate && \
    uv pip install -e .

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]