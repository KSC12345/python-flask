import os
from playwright.sync_api import sync_playwright

# Get the path from the environment variable (set in Docker)
playwright_browsers_path = os.environ.get("PLAYWRIGHT_BROWSERS_PATH", "/home/appuser/playwright-browsers")

# Construct the Chromium binary path
chromium_path = f"{playwright_browsers_path}/chromium-*/chrome-linux/chrome"

with sync_playwright() as p:
    browser = p.chromium.launch(
        executable_path=chromium_path,  # Explicit path
        headless=True
    )
