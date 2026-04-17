from pages.base_page import BasePage

class ProductPage(BasePage):

    ADD_TO_CART = "//a[text()='Add to cart']"

    async def wait_for_page(self):
        await self.page.wait_for_selector(self.ADD_TO_CART)

    async def add_to_cart(self):
        async with self.page.expect_event("dialog", timeout=3000) as dialog_info:
            await self.click(self.ADD_TO_CART)

        dialog = await dialog_info.value
        message = dialog.message
        await dialog.accept()

        return message