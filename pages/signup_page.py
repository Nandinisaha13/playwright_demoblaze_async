from pages.base_page import BasePage


class SignupPage(BasePage):
    SIGNUP_BTN = "#signin2"
    USERNAME = "#sign-username"
    PASSWORD = "#sign-password"
    SUBMIT = "button[onclick='register()']"

    async def open_signup_modal(self):
        await self.click(self.SIGNUP_BTN)
        await self.page.wait_for_selector("#sign-username", state="visible")

    async def signup(self, username, password):
        await self.fill(self.USERNAME, username)
        await self.fill(self.PASSWORD, password)

        try:
            async with self.page.expect_event("dialog", timeout=5000) as dialog_info:
                await self.click(self.SUBMIT)

            dialog = await dialog_info.value
            message = dialog.message
            await dialog.accept()
            return message

        except:
            return None