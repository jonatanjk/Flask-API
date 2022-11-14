import requests


def main():
    response = requests.post("http://127.0.0.1:5000/getdata", json={'number': '12524', 'type': 'issue', 'action': 'show'})
    print(response.json())

if __name__ == "__main__":
    main()