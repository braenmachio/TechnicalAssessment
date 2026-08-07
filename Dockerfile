# Builder Image
FROM ubuntu:26.04 AS builder

# we use uv for our tooling
COPY --from=ghcr.io/astral-sh/uv:0.12.2-python3.13-trixie /uv /uvx /usr/local/bin/

RUN apt-get update ; apt-get install -y --no-install-recommends \
    python3 build-essentials libpq-dev ; rm -rf /var/lib/apt/lists/*

WORKDIR /build

COPY my_app/requirements.txt .

# using uv create a v. env and install packages
RUN uv venv /opt/venv ; uv pip install --python /opt/venv/bin/python --no-cache requirements.txt

# Mininmal Runtime Image
FROM ubuntu:26.04

RUN apt-get update ; apt-get install -y --no-install-recommends \
    python3 libpq5 ; rm -rf /var/lib/apt/lists/*

COPY --from=builder /opt/venv /opt/venv
ENV PATH="opt/venv/bin:$PATH"

WORKDIR /app
COPY my_app/my_app ./my_app

CMD [ "python3", "my_app/main.py" ]