import pytest

from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.product_page import ProductPage

@pytest.mark.asyncio
async def test_delete_product_from_cart(page):
    home = HomePage(page)
    product = ProductPage(page)
    cart = CartPage(page)

    products_to_add=[
        "Samsung galaxy s6",
        "Nokia lumia 1520",
        "Nexus 6"
    ]

    for item in products_to_add:
        await home.select_product_by_name(item)
        await product.wait_for_page()
        await product.add_to_cart()
        await home.go_to_home()

    await cart.open_cart()
    cart_items = await cart.get_product_names()

    for item in products_to_add:
        assert item in cart_items

    await cart.delete_all_products()
    assert await cart.is_cart_empty()