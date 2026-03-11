set shell := ["bash", "-eu", "-o", "pipefail", "-c"]
set dotenv-load := true

VENV_DIR := ".venv"

default:
    @just --list

venv:
    @uv venv {{ VENV_DIR }}

sync:
    @uv sync

setup: venv sync

upgrade:
    @uv lock --upgrade

lock:
    @uv lock

test:
    @uv run --group=test pytest --cov

lint:
    @uv run --group=lint ty check
    @uv run --group=lint ruff format --preview --check
    @uv run --group=lint ruff check --show-fixes --preview

fmt:
    @uv run --group=lint ruff format --preview

check: fmt lint test
