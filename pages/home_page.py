from conftest import page
from pages.base_page import BasePage
class HomePage(BasePage):

    async def select_product_by_name(self, product_name):
        await self.page.get_by_role("link", name=product_name).click()

    async def go_to_home(self):
        await self.page.get_by_role("link", name="Home (current)").click()