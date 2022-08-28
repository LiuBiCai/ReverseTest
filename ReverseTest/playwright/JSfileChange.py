from playwright.sync_api import sync_playwright

Base_URL='https://spa2.scrape.center'
context=sync_playwright().start()
browser=context.chromium.launch()
page=browser.new_page()
page.route(
	"/js/chunk-10192a00.243cb8b7.js",
	lambda route: route.fulfill(path="./chunk.js")
)
page.goto(Base_URL)
