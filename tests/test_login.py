import pytest
from pages.login_page import LoginPage

@pytest.mark.asyncio
async def test_valid_login(page):

    login_page = LoginPage(page)

    await login_page.open_login_modal()

    alert = await login_page.login("QA Check", "Password")

    # No alert expected
    assert alert is None

    # Validate login success
    await page.wait_for_selector("#nameofuser")

    user_text = await login_page.get_logged_user()

    assert "Welcome" in user_text