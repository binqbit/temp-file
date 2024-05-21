
import sys
import pyperclip
import requests

if len(sys.argv) > 1:
    file_name = sys.argv[1]
    response = requests.request('POST', 'https://tmpfiles.org/api/v1/upload', files={'file': open(file_name, 'rb')})
    url = response.json()['data']['url'].replace('https://tmpfiles.org/', 'https://tmpfiles.org/dl/')
    curl = f'curl -o {file_name} {url}'
    print(curl)
    pyperclip.copy(curl)
else:
    curl = 'curl https://tmpfiles.org/api/v1/upload -F "file=@/"';
    print(curl)
    pyperclip.copy(curl)