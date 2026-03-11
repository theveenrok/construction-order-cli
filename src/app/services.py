from app.exporters import BaseOrderExporter
from app.entities import CommercialOffer, Product, Order


def create_offer(product: Product, discount: float = 0) -> CommercialOffer:
    """Create a commercial offer for the given product with an optional discount."""
    total_price = round(product.price * (1 - discount), 2)
    return CommercialOffer(product=product, total_price=total_price)

def place_order(offer: CommercialOffer, exporter: BaseOrderExporter) -> Order:
    """Place an order and export it using the provided exporter."""
    order = Order(
        region=offer.product.region,
        product_name=offer.product.name,
        product_category=offer.product.category,
        total_price=offer.total_price,
    )
    exporter.export(order)
    return order    