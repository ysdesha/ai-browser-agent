import asyncio

from playwright.async_api import (
    async_playwright,
    TimeoutError as PlaywrightTimeoutError
)


async def tab_manager():

    urls = [
        "https://google.com",
        "https://github.com",
        "https://python.org",
        "https://news.ycombinator.com",
        "https://stackoverflow.com"
    ]

    try:

        async with async_playwright() as p:

            browser = await p.chromium.launch(
                headless=False
            )

            pages = []

            # Create 5 tabs
            for _ in urls:
                page = await browser.new_page()
                pages.append(page)

            # Open all tabs in parallel
            try:

                tasks = []

                for page, url in zip(pages, urls):

                    tasks.append(
                        page.goto(
                            url,
                            timeout=10000
                        )
                    )

                await asyncio.gather(*tasks)

            except PlaywrightTimeoutError:

                print(
                    "Error: One or more pages timed out while loading."
                )

                await browser.close()
                return

            print("\nPage Titles:\n")

            # Capture titles
            for i, page in enumerate(pages):

                try:

                    title = await page.title()

                    print(
                        f"Tab {i+1}: {title}"
                    )

                except Exception:

                    print(
                        f"Error: Could not retrieve title for Tab {i+1}"
                    )

            # Keep first tab open
            first_page = pages[0]

            # Close remaining tabs
            for page in pages[1:]:

                try:

                    await page.close()

                except Exception:

                    print(
                        "Error: Could not close a tab."
                    )

            print(
                "\nClosed all tabs except the first."
            )

            print(
                "Keeping first tab open for 5 seconds..."
            )

            await first_page.wait_for_timeout(
                5000
            )

            await browser.close()

    except Exception as e:

        print(
            f"Unexpected Error: {e}"
        )


asyncio.run(tab_manager())