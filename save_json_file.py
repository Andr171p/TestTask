import requests
import json


def get_json_response():
    url = "https://testtask-production.up.railway.app/api/users/users/"
    response = requests.get(url=url)
    return response.json()


def save_json_file(data):
    with open("test_task.json", "w") as file:
        json.dump(data, file, ensure_ascii=False)


def main():
    json_data = get_json_response()
    save_json_file(data=json_data)


if __name__ == "__main__":
    main()
