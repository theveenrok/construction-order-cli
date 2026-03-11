import json
from pathlib import Path

from app.entities import Product


def load_products_from_json_file(path: Path) -> list[Product]:
    with open(path, "r") as f:
        data = json.load(f)
    return [Product(**item) for item in data]
