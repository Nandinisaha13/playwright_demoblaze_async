import random

from pages.signup_page import SignupPage
import pytest

@pytest.mark.asyncio
async def test_signup_new_user(page):

    signup_page= SignupPage(page)

    await signup_page.open_signup_modal()

    # unique username every time
    username = f"user_{random.randint(1000,9999)}"
    alert = await signup_page.signup(username, "test123")
    assert alert == "Sign up successful."
