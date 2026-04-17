import sys
import os
import pytest
from playwright.async_api import async_playwright

# Fix import path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

@pytest.fixture
async def page():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto("https://www.demoblaze.com")
        yield page
        await browser.close()