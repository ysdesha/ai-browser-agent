from agent import llm

from browser_tools import (
    navigate_to,
    click_element,
    type_text
)

from memory_store import (
    get_user_profile
)

profile = get_user_profile()

print("\nUSER PROFILE")
print(profile)

print("\nAVAILABLE TOOLS")
print(navigate_to.name)
print(click_element.name)
print(type_text.name)

command = "Go to google.com and search for AI news"

print("\nUSER COMMAND:")
print(command)

print("\nAGENT REASONING:")

navigate_result = navigate_to.invoke(
    {"url": "https://www.google.com"}
)

print("OBSERVATION:", navigate_result)

type_result = type_text.invoke(
    {"text": "AI news"}
)

print("OBSERVATION:", type_result)

print("\nFINAL RESULT:")
print("Task completed")