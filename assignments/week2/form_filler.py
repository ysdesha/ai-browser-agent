import asyncio
import json

from playwright.async_api import (
    async_playwright,
    TimeoutError as PlaywrightTimeoutError
)


async def form_filler():

    try:
        # Load user data from JSON
        with open("user_data.json", "r", encoding="utf-8") as file:
            user = json.load(file)

        async with async_playwright() as p:

            browser = await p.chromium.launch(
                headless=False
            )

            page = await browser.new_page()

            # Error Condition 1: Page load timeout
            try:
                await page.goto(
                    "https://demoqa.com/automation-practice-form",
                    timeout=10000
                )

            except PlaywrightTimeoutError:
                print("Error: Page load timed out")
                await browser.close()
                return

            # Error Condition 2: Element not found
            try:
                await page.fill(
                    "#firstName",
                    user["first_name"]
                )

            except Exception:
                print("Error: First Name field not found")
                await browser.close()
                return

            # Fill remaining fields
            await page.fill(
                "#lastName",
                user["last_name"]
            )

            await page.fill(
                "#userEmail",
                user["email"]
            )

            # Select Female radio button
            await page.locator(
                "label[for='gender-radio-2']"
            ).click()

            await page.fill(
                "#userNumber",
                user["mobile"]
            )

            await page.fill(
                "#currentAddress",
                user["address"]
            )

            # Screenshot before submission
            await page.screenshot(
                path="form_filled.png",
                full_page=True
            )

            print("Form filled successfully.")
            print("Screenshot saved as form_filled.png")

            await page.wait_for_timeout(5000)

            await browser.close()

    except FileNotFoundError:
        print("Error: user_data.json not found")

    except json.JSONDecodeError:
        print("Error: Invalid JSON format")

    except Exception as e:
        print(f"Unexpected Error: {e}")


asyncio.run(form_filler())