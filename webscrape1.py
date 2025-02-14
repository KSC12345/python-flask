from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Get the Chromium executable path
    browser_path = p.chromium.executable_path
    
    # Launch browser with explicit path
    browser = p.chromium.launch(
        executable_path=browser_path,  # Use the retrieved path
        headless=True
    )
    
    # Example usage
    page = browser.new_page()
    page.goto("https://example.com")
    page.screenshot(path="example.png")
    browser.close()
