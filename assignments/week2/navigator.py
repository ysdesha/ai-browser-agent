import asyncio
import json

from playwright.async_api import (
    async_playwright,
    TimeoutError as PlaywrightTimeoutError
)


async def navigator():

    try:
        async with async_playwright() as p:

            browser = await p.chromium.launch(
                headless=False
            )

            page = await browser.new_page()

            try:
                await page.goto(
                    "https://news.ycombinator.com",
                    timeout=10000
                )

            except PlaywrightTimeoutError:
                print("Error: Page load timed out")
                await browser.close()
                return

            try:
                await page.wait_for_selector(
                    ".titleline",
                    timeout=5000
                )

            except PlaywrightTimeoutError:
                print("Error: Article titles not found")
                await browser.close()
                return

            titles = page.locator(".titleline")

            count = await titles.count()

            if count == 0:
                print("Error: No articles found")
                await browser.close()
                return

            articles = []

            for i in range(min(5, count)):

                article = titles.nth(i)

                text = await article.text_content()

                articles.append(
                    {
                        "rank": i + 1,
                        "title": text
                    }
                )

            with open(
                "articles.json",
                "w",
                encoding="utf-8"
            ) as file:

                json.dump(
                    articles,
                    file,
                    indent=4,
                    ensure_ascii=False
                )

            await page.screenshot(
                path="navigator_screenshot.png"
            )

            print("\nTop 5 Articles:\n")

            for article in articles:
                print(
                    f"{article['rank']}. {article['title']}"
                )

            print(
                "\nArticles saved to articles.json"
            )

            await browser.close()

    except Exception as e:
        print(f"Unexpected Error: {e}")


asyncio.run(navigator())