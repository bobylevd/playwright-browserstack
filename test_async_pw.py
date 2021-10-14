import json
from urllib.parse import quote_plus

import pytest
from playwright.async_api import async_playwright


@pytest.mark.asyncio
async def test_async_pw(caps):
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp(f"wss://cdp.browserstack.com/playwright?caps={quote_plus(json.dumps(caps))}", timeout=60000)

        page = await browser.new_page()
        await page.goto("https://google.com/ncr")
        title = await page.title()
        assert title == "Google"
        await browser.close()
