class BasePage:
    def __init__(self, page):
        self.page= page

    async def click(self, locator):
        await self.page.locator(locator).click()

    async def fill(self, locator, value):
        await self.page.locator(locator).fill(value)

    async def get_text(self, locator):
        return await self.page.locator(locator).inner_text()