from conftest import page
from pages.base_page import BasePage
class HomePage(BasePage):
    PRODUCT = "//a[text()='Samsung galaxy s6']"

    async def select_product(self):
        await self.click(self.PRODUCT)