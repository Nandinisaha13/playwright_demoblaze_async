from pages.base_page import BasePage

class LoginPage(BasePage):

    LOGIN_BTN = "#login2"
    USERNAME = "#loginusername"
    PASSWORD = "#loginpassword"
    SUBMIT_BTN = "button[onclick='logIn()']"
    LOGGED_USER = "#nameofuser"

    async def open_login_modal(self):
        await self.click(self.LOGIN_BTN)
        await self.page.wait_for_selector("#loginusername", state="visible")

    async def login(self, username, password):
        await self.fill(self.USERNAME, username)
        await self.fill(self.PASSWORD, password)


        try:
            async with self.page.expect_event("dialog", timeout=3000) as dialog_info:
                await self.click(self.SUBMIT_BTN)

            dialog = await dialog_info.value
            message = dialog.message
            await dialog.accept()
            return message

        except:
            return None
    async def get_logged_user(self):
        return await self.get_text(self.LOGGED_USER)