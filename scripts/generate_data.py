import dataclasses


def generate_products_data() -> None:
    """Generate sample products data and save it to a JSON file `products.json`."""
    import json
    from pathlib import Path

    from app.entities import Product
    products = []
    products = [
        Product(id=1, name="Бетон М100", price=5000, region="Москва", category="Бетон"),
        Product(id=2, name="Бетон М300", price=9000, region="Москва", category="Бетон"),
        Product(id=3, name="Кирпич керамический", price=100, region="Москва", category="Кирпич"),
        Product(id=4, name="Кирпич красный", price=50, region="Санкт-Петербург", category="Кирпич"),
        Product(id=5, name="Кирпич силикатный", price=40, region="Санкт-Петербург", category="Кирпич"),
        Product(id=6, name="Кирпич керамический", price=60, region="Санкт-Петербург", category="Кирпич"),
        Product(id=7, name="Песок строительный", price=1000, region="Новосибирск", category="Песок"),
        Product(id=8, name="Бетон М300", price=6000, region="Новосибирск", category="Бетон"),
        Product(id=9, name="Песок речной", price=1200, region="Новосибирск", category="Песок"),
        Product(id=10, name="Песок карьерный", price=800, region="Новосибирск", category="Песок"),
        
    ]

    output_path = Path("products.json")
    with output_path.open("w") as f:
        json.dump([dataclasses.asdict(p) for p in products], f, ensure_ascii=False, indent=4)

    print(f"Sample products data has been generated and saved to {output_path.absolute()}")