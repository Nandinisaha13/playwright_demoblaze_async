import pytest
from pages.login_page import LoginPage

test_data = [
    ("Popular", "correct", "User does not exist."),  
    ("QA Check", "wrongpass", "Wrong password."),
    ("", "Password", None),   
    ("testuser", "", None),
    ("", "", None),
]

@pytest.mark.asyncio
@pytest.mark.parametrize("username,password,expected_alert", test_data)
async def test_invalid_login(page, username, password, expected_alert):

    login_page = LoginPage(page)
    await login_page.open_login_modal()
    alert = await login_page.login(username, password)
    assert alert == expected_alert
   