from __future__ import annotations
import uuid

import dataclasses


@dataclasses.dataclass
class Product:
    """Construction product.

    Attributes:

        name: Product name.
        price: Product price in rubles.
        category: Product category.
        region: Region of sale.
    """

    id: int
    name: str
    price: float
    category: str
    region: str


@dataclasses.dataclass
class CommercialOffer:
    """Comercial offer for a product.
    Used when forming an order.

    Attributes:

         product: Product for which the offer is made.
         total_price: Total price of the offer in rubles."""

    product: Product
    total_price: float


@dataclasses.dataclass
class Order:
    """Order for a product.

    Attributes:

        region: Region of sale.
        product_name: Product name.
        product_category: Product category.
        total_price: Total price of the order in rubles.
    """

    id: int
    region: str
    product_name: str
    product_category: str
    total_price: float
