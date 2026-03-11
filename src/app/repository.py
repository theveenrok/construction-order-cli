from collections.abc import Sequence

from app.entities import Product


class BaseProductRepository:
    def get_products_by_region(self, region: str) -> Sequence[Product]:
        raise NotImplementedError

    def get_cheaper_alternative(self, product: Product) -> Product | None:
        raise NotImplementedError

    def get_available_region_names(self) -> Sequence[str]:
        raise NotImplementedError


class InMemoryProductRepository(BaseProductRepository):
    """Product repository that stores products in memory."""

    def __init__(self, products: Sequence[Product]):
        self._products = products

    def get_products_by_region(self, region: str) -> Sequence[Product]:
        return [p for p in self._products if p.region == region]

    def get_cheaper_alternative(self, product: Product) -> Product | None:
        filtered = filter(lambda p: p.region == product.region and p.category == product.category and p.price < product.price, self._products)
        return next(filtered, None,)

    def get_available_region_names(self) -> Sequence[str]:
        return sorted(set(p.region for p in self._products))
