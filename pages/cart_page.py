from pages.base_page import BasePage

class CartPage(BasePage):

    CART_BTN = "#cartur"
    PRODUCT_NAME = ".success td:nth-child(2)"

    async def open_cart(self):
        await self.click(self.CART_BTN)
        await self.page.wait_for_selector(".success")

    async def get_product_names(self):
        return await self.page.locator(self.PRODUCT_NAME).all_inner_texts()