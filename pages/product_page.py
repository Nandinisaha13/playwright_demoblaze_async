from pages.base_page import BasePage

class ProductPage(BasePage):

    async def wait_for_page(self):
        await self.page.get_by_text("Add to cart", exact=True).wait_for()

    async def add_to_cart(self):
        async with self.page.expect_event("dialog", timeout=3000) as dialog_info:
            await self.page.get_by_text("Add to cart", exact=True).click()

        dialog = await dialog_info.value
        message = dialog.message
        await dialog.accept()

        return message