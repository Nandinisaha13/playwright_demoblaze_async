from conftest import page
from pages.base_page import BasePage
class HomePage(BasePage):

    async def select_product(self):
        await self.page.get_by_role("link", name="Samsung galaxy s6").click()