from pathlib import Path
from typing import Annotated

import questionary
import typer

from app.exporters import OrderJsonExporter
from app.loader import load_products_from_json_file
from app.repository import InMemoryProductRepository
from app.services import create_alternative_offer_or_sale, create_offer, place_order


def cli(
    products_path: Annotated[Path, typer.Option(help="Путь к JSON файлу с данными о продуктах")],
    order_path: Annotated[Path, typer.Option(help="Путь к JSON файлу с данными о заказе")],
):
    # Initialize repositories.
    product_repository = InMemoryProductRepository(products=load_products_from_json_file(products_path))

    # Get available region names.
    available_region_names = product_repository.get_available_region_names()

    if not available_region_names:
        typer.echo("Нет доступных регионов для заказа.")
        exit()

    # Request region selection.
    region = questionary.select(message="Выберите Регион", choices=available_region_names).ask()

    # Get products by region.
    products_by_region = product_repository.get_products_by_region(region)

    if not products_by_region:
        typer.echo(f"Нет доступных товаров для региона {region}.")
        exit()

    # Request product selection.
    product_selected = questionary.select(
        message="Выберите товар",
        choices=[questionary.Choice(title=f"{p.name} ({p.price} руб.)", value=p) for p in products_by_region],
    ).ask()

    # Create commercial offer for the selected product.
    offer = create_offer(product_selected)

    # Confirm order creation.
    confirmation_create_order = questionary.confirm(
        message=f"Вы хотите создать заказ на {offer.product.name} ({offer.total_price} руб.)?"
    ).ask()

    if not confirmation_create_order:
        # Customer retention in case of refusal to create an order for the initially selected product.

        # Create an alternative offer.
        offer = create_alternative_offer_or_sale(product=product_selected, repository=product_repository)

        # Confirm order creation for the alternative offer.
        confirmation_create_order = questionary.confirm(
            message=f"Возможно вам подойдет {offer.product.name} за ({offer.total_price} руб.)?",
        ).ask()

        if not confirmation_create_order:
            exit()

    # Place order.
    order = place_order(offer, exporter=OrderJsonExporter(order_path))
    typer.echo(
        message=(
            f"Заказ успешно создан! (Сохранен по пути `{order_path.absolute()}`)\n"
            f"ID: {order.id}\n"
            f"Регион: {order.region}\n"
            f"Товар: {order.product_name}\n"
            f"Категория: {order.product_category}\n"
            f"Итоговая цена: {order.total_price} руб."
        )
    )


def main() -> None:
    typer.run(cli)
    
if __name__ == "__main__":
    main()