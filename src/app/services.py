from app.entities import CommercialOffer, Order, Product
from app.exporters import BaseOrderExporter
from app.repository import BaseProductRepository


def create_offer(product: Product, discount: float = 0) -> CommercialOffer:
    """Create a commercial offer for the given product with an optional discount."""
    total_price = round(product.price * (1 - discount), 2)
    return CommercialOffer(product=product, total_price=total_price)


def create_alternative_offer_or_sale(product: Product, repository: BaseProductRepository) -> CommercialOffer:
    """Create an alternative commercial offer for the given product, otherwise offer the same product at a discount."""
    alternative_product = repository.get_cheaper_alternative(product)
    if alternative_product:
        return create_offer(alternative_product)
    else:
        return create_offer(product, discount=0.05)  # Offer a 10% discount if no alternatives are available


def place_order(offer: CommercialOffer, exporter: BaseOrderExporter) -> Order:
    """Place an order and export it using the provided exporter."""
    order = Order(
        id=1,  # In a real application, you would generate a unique ID or use a database auto-increment.
        region=offer.product.region,
        product_name=offer.product.name,
        product_category=offer.product.category,
        total_price=offer.total_price,
    )
    exporter.export(order)
    return order
