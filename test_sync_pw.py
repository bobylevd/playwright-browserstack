import json
from urllib.parse import quote_plus

from playwright.sync_api import sync_playwright


def test_sync_pw(caps):
    with sync_playwright() as p:
        browser = p.chromium.connect(f"wss://cdp.browserstack.com/playwright?caps={quote_plus(json.dumps(caps))}", timeout=60000)
        # browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://google.com/ncr")
        title = page.title()
        assert title == "Google"
        browser.close()
