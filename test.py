import requests

def check_server_status(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return "Server is up"
        else:
            return f"Server returned status code: {response.status_code}"
    except requests.ConnectionError:
        return "Server is down"

url = "ftp.cisco.com"
status = check_server_status(url)
print(status)