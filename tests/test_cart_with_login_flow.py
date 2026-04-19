import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

@pytest.mark.asyncio
async def test_add_multiple_products_after_login(page):

    login = LoginPage(page)
    home = HomePage(page)
    product = ProductPage(page)
    cart = CartPage(page)

    # Step 1: Login
    await login.open_login_modal()
    alert = await login.login("QA Check", "Password")

    assert alert is None
    await page.wait_for_selector("#nameofuser")
    await home.select_product_by_name("Samsung galaxy s6")
    await product.wait_for_page()

    alert = await product.add_to_cart()
    assert alert == "Product added."
    await home.go_to_home()
    await home.select_product_by_name("Nokia lumia 1520")
    await product.wait_for_page()
    alert = await product.add_to_cart()
    assert alert == "Product added."

    await cart.open_cart()
    products = await cart.get_product_names()
    assert "Samsung galaxy s6" in products
    assert "Nokia lumia 1520" in products