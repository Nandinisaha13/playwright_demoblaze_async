import pytest

from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.order_modal import OrderModal
from pages.product_page import ProductPage

@pytest.mark.asyncio
async def test_checkout(page):
    login= LoginPage(page)
    home= HomePage(page)
    cart = CartPage(page)
    product= ProductPage(page)
    orderModal = OrderModal(page)

    await login.open_login_modal()
    await login.login("QA Check", "Password")

    products_to_add =["Iphone 6 32gb", "Sony vaio i5", "Nexus 6"]

    for item in products_to_add:
        await home.select_product_by_name(item)
        await product.wait_for_page()
        await product.add_to_cart()
        await home.go_to_home()

    await cart.open_cart()
    await cart.place_order()

    await orderModal.fill_order_details({
        "name": "QA",
        "country": "India",
        "city": "Mumbai",
        "card": "1234567890123456",
        "month": "04",
        "year": "2026"
    })

    await orderModal.purchase()

    success_message= page.get_by_role("heading", name="Thank you for your purchase!")
    assert await success_message.text_content() == "Thank you for your purchase!"

    details = await page.locator("p.lead.text-muted").text_content()

    assert "Id" in details
    assert "Amount" in details
    assert "Card Number" in details

    await page.get_by_role("button", name="OK").click()
