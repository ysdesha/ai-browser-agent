import json


def get_user_profile():

    with open(
        "user_profile.json",
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)