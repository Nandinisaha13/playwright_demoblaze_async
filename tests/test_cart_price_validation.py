import pytest

from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.product_page import ProductPage

@pytest.mark.asyncio
async def test_multiple_products_price_validation(page):

    home= HomePage(page)
    product= ProductPage(page)
    cart= CartPage(page)

    products_to_add =["Iphone 6 32gb", "Sony vaio i5", "Nexus 6"]

    for item in products_to_add:
        await home.select_product_by_name(item)
        await product.wait_for_page()
        await product.add_to_cart()
        await home.go_to_home()

    await cart.open_cart()

    prices = await cart.get_product_prices()
    expected_total= sum(prices)

    actual_total= await cart.get_total_prices()

    assert expected_total == actual_total
