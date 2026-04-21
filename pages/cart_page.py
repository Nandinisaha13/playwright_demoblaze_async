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
            initial_count = await rows.count()

            # always click first row's delete
            await rows.first.get_by_role("link", name="Delete").click()

            # wait until count decreases
            await self.page.wait_for_function(
    """(args) => 
        document.querySelectorAll(args.selector).length < args.count
    """,
    arg={"selector": ".success", "count": initial_count}
)

    async def is_cart_empty(self):
        return await self.page.locator(".success").count() == 0
    
    async def get_product_prices(self):
        prices = await self.page.locator("td:nth-child(3)").all_inner_texts()
        return [int(price) for price in prices]
    
    async def get_total_prices(self):
        total = await self.page.locator("#totalp").inner_text()
        return int(total)
    
    async def place_order(self):
        await self.page.get_by_role("button", name="Place Order").click()