from pages.base_page import BasePage


class OrderModal(BasePage):
    def __init__(self, page):
        self.page = page

        self.name= page.locator("#name")
        self.country= page.locator("#country")
        self.city= page.locator("#city")
        self.card= page.locator("#card")
        self.month= page.locator("#month")
        self.year= page.locator("#year")

        self.button= page.get_by_role("button", name="Purchase")

    async def fill_order_details(self, data):
        await self.name.fill(data["name"])
        await self.country.fill(data["country"])
        await self.city.fill(data["city"])
        await self.card.fill(data["card"])
        await self.month.fill(data["month"])
        await self.year.fill(data["year"])

    async def purchase(self):
        await self.button.click()

