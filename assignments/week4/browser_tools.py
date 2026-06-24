from langchain.tools import tool


@tool
def navigate_to(url: str) -> str:
    """
    Navigate to a website.
    """

    print(f"\n[TOOL] Navigating to: {url}")

    return f"Opened {url}"


@tool
def click_element(selector: str) -> str:
    """
    Click an element using a CSS selector.
    """

    print(f"\n[TOOL] Clicking: {selector}")

    return f"Clicked {selector}"


@tool
def type_text(text: str) -> str:
    """
    Type text into a page.
    """

    print(f"\n[TOOL] Typing: {text}")

    return f"Typed {text}"