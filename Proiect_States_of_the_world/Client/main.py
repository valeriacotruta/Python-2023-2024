import requests
import json


def verify_error_code(result):
    try:
        return json.dumps(result.json())
    except requests.exceptions.JSONDecodeError as exception:
        return exception


if __name__ == "__main__":
    API_URL = "http://127.0.0.1:8080/"
    print("Enter the endpoint: ")
    endpoint = None
    while True:
        try:
            endpoint = input()
            URL = API_URL + endpoint
            result = requests.get(URL)
            if result.status_code == 200:
                print(verify_error_code(result))
            else:
                result = requests.post(URL)
                if result.status_code == 200:
                    print(verify_error_code(result))
                else:
                    raise requests.exceptions.RequestException("The request failed!")
        except requests.exceptions.RequestException as exception:
            print(exception)
            break
