from python:3.12-alpine as base

RUN apk add --no-cache \
    build-base \
    libffi-dev \
    linux-headers \
    musl-dev \
    postgresql-dev \
    python3-dev \
    py3-pip

CMD ["python3", "-m", "main.py", "8000"]