import requests
import json


def get_token():

    url = ""

    payload = "{}"
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
        'Content-Type': 'application/json;charset=UTF-8',
        'Cookie': 'JSESSIONID=eb3dbcbd-3bf5-47d5-9f0d-7934e3c52be4'}

    response = requests.request(
        "POST",
        url,
        headers=headers,
        data=payload).content
    response = json.loads(response.decode())["data"]["token"]
    return response
