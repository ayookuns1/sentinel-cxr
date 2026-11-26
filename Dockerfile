# Small image with Python 3.12 and uv preinstalled.
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

WORKDIR /app

# 1) Dependencies first. This layer is cached until pyproject.toml / uv.lock change,
#    so editing your code does not re-download everything on every build.
COPY pyproject.toml uv.lock README.md ./
RUN uv sync --locked --no-dev --no-install-project

# 2) Then the code itself.
COPY src ./src
COPY configs ./configs
RUN uv sync --locked --no-dev

# Run as a normal user, not root.
RUN useradd --create-home sentinel && chown -R sentinel /app
USER sentinel

ENV PATH="/app/.venv/bin:$PATH"
CMD ["sentinel-train"]
