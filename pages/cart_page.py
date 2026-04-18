from pages.base_page import BasePage

class CartPage(BasePage):

    async def open_cart(self):
        await self.page.get_by_text("Cart", exact=True).click()
        await self.page.wait_for_selector(".success")

    async def get_product_names(self):
        return await self.page.locator("td").filter(has_text="Samsung galaxy s6").all_inner_texts()