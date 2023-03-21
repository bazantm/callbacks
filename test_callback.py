import requests


def make_request(url, callback):
    response = requests.get(url)
    callback(response)


def handle_response(response):
    if response.status_code == 200:
        data = response.json()
        print('Data received: ', data)
    else:
        print('Error: ', response.status_code)


if __name__ == '__main__':
    make_request('http://api.open-notify.org/astros.json', handle_response)