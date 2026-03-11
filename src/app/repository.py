from collections.abc import Sequence

from app.entities import Product


class BaseProductRepository:
    def get_products_by_region(self, region: str) -> Sequence[Product]:
        raise NotImplementedError

    def get_products_by_region_and_category(self, region: str, category: str) -> Sequence[Product]:
        raise NotImplementedError

    def get_available_region_names(self) -> Sequence[str]:
        raise NotImplementedError


class InMemoryProductRepository(BaseProductRepository):
    """Product repository that stores products in memory."""

    def __init__(self, products: Sequence[Product]):
        self._products = products

    def get_products_by_region(self, region: str) -> Sequence[Product]:
        return [p for p in self._products if p.region == region]

    def get_products_by_region_and_category(self, region: str, category: str) -> Sequence[Product]:
        return [p for p in self._products if p.region == region and p.category == category]

    def get_available_region_names(self) -> Sequence[str]:
        return sorted(set(p.region for p in self._products))
