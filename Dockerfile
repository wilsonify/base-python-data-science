FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

COPY src/data-scratch-library /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        nodejs \
        npm \
        g++ \
        gcc \
        make \
        cmake \
    && python -m pip install --upgrade pip \
    && pip install . \
    && rm -rf /var/lib/apt/lists/*

HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
    CMD python -c "import dsl" || exit 1

CMD ["python", "-c", "import dsl; print('dsl container ready')"]
