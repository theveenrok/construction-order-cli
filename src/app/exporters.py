import dataclasses
import json
from pathlib import Path

from app.entities import Order


class BaseOrderExporter:
    def __init__(self, path: Path):
        self._path = path

    def export(self, order: Order):
        raise NotImplementedError


class OrderJsonExporter(BaseOrderExporter):
    """Order exporter that saves orders in JSON format."""

    def export(self, order: Order):
        self._path.parent.mkdir(parents=True, exist_ok=True)
        with open(self._path, "w", encoding="utf-8") as file:
            json.dump(
                dataclasses.asdict(order),
                file,
                indent=2,
                ensure_ascii=False,
            )
