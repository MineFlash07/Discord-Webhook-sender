import json
import requests


data = {
    "url": "",
    "webhook": {
        "content": "This is a cool webhook"
    }
}


def main():
    global data
    try:
        with open("settings.json") as fileout:
            data = json.load(fileout)
    except FileNotFoundError:
        print_system_message("Settings file does not exit")
        write_in_settings(data)
        return
    if "url" not in data:
        print_system_message("Url setting does not exit")
        data["url"] = ""
        write_in_settings(data)
        return
    if "webhook" not in data:
        print_system_message("Webhook setting does not exit")
        data["webhook"] = {
            "content": "This is a cool webhook"
        }
        write_in_settings(data)
        return
    requests.post(data["url"], data=data["webhook"])



def print_system_message(message: str):
    print("=====================================================")
    print(message)
    print("=====================================================")


def write_in_settings(file_input):
    with open("settings.json", "w") as fileout:
        fileout.write(json.dumps(file_input, indent=4))


if __name__ == '__main__':
    main()
