from pages.base_page import BasePage

class CartPage(BasePage):

    async def open_cart(self):
        await self.page.get_by_text("Cart", exact=True).click()
        await self.page.locator(".success").first.wait_for()
        
    async def get_product_names(self):
        return await self.page.locator(".success td:nth-child(2)").all_inner_texts()