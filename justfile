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

generate-data:
    @uv run generate-data

[arg("PRODUCTS_PATH", long="products-path")]
[arg("ORDER_PATH", long="order-path")]
run PRODUCTS_PATH ORDER_PATH:
    @uv run cli --products-path="{{ PRODUCTS_PATH }}" --order-path="{{ ORDER_PATH }}"