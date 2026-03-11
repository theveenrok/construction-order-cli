from app.entities import CommercialOffer, Product


def create_offer(product: Product, discount: float = 0) -> CommercialOffer:
    """Create a commercial offer for the given product with an optional discount."""
    total_price = round(product.price * (1 - discount), 2)
    return CommercialOffer(product=product, total_price=total_price)
