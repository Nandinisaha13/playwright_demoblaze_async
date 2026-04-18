import pytest

from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.product_page import ProductPage

@pytest.mark.asyncio
async def test_add_product_to_cart(page):
    home = HomePage(page)
    product = ProductPage(page)
    cart = CartPage(page)

    await home.select_product()
    await product.wait_for_page()
    alert = await product.add_to_cart()
    assert alert == "Product added"
    await cart.open_cart()
    products = await cart.get_product_names()
    assert "Samsung galaxy s6" in products