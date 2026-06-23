import asyncio
import json

async def load_user():

    try:

        with open("user.json", "r") as f:
            data = json.load(f)

        print("\nUser Information")
        print("----------------")

        print(f"Name: {data['name']}")
        print(f"Email: {data['email']}")
        print(f"Phone: {data['phone']}")
        print(f"Address: {data['address']}")

    except FileNotFoundError:
        print("user.json not found")

asyncio.run(load_user())