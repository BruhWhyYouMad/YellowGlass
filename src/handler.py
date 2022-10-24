import json


def message_handler(raw, display):
    data = json.loads(raw)
    if data["message"] != "":
        display(data["message"], "Bob")
