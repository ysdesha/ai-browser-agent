from intent_parser import parse_intent
import time

commands = [
    "open google",
    "close all tabs",
    "apply to this job",
    "email this summary to my boss",
    "summarize this article",
    "click submit",
    "open linkedin",
    "fill this registration form",
    "search for AI jobs",
    "send this report by email"
]

for command in commands:

    print("\n" + "=" * 50)
    print("COMMAND:", command)

    result = parse_intent(command)

    print(result)

    time.sleep(15)