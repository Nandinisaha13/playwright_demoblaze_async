from pages.base_page import BasePage

class CartPage(BasePage):

    async def open_cart(self):
        await self.page.get_by_text("Cart", exact=True).click()
        await self.page.locator(".success").first.wait_for()
        
    async def get_product_names(self):
        return await self.page.locator(".success td:nth-child(2)").all_inner_texts()
    
    async def delete_all_products(self):
        rows = self.page.locator(".success")
        while await rows.count() > 0:
            row = rows.first
            delete_btn = row.get_by_role("link", name="Delete")
            await delete_btn.click()
            await row.wait_for(state="detached")

    async def is_cart_empty(self):
        return await self.page.locator(".success").count() == 0