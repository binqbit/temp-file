
import os
import sys
import pyperclip
import requests
from zipfile import ZipFile

if len(sys.argv) > 1:
    file_name = sys.argv[1]
    if file_name.endswith('/') or file_name.endswith('\\'):
        file_name = file_name[:-1]
    is_dir = os.path.isdir(file_name)
    if is_dir:
        with ZipFile(file_name + '.zip', 'w') as zip:
            for root, dirs, files in os.walk(file_name):
                for file in files:
                    zip.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), os.path.join(file_name, '..')))
        file_name = file_name + '.zip'
        
    response = requests.request('POST', 'https://tmpfiles.org/api/v1/upload', files={'file': open(file_name, 'rb')})
    os.remove(file_name)
    url = response.json()['data']['url'].replace('https://tmpfiles.org/', 'https://tmpfiles.org/dl/')
    cmd = f'curl -o {file_name} {url}'
    if is_dir:
        cmd = cmd + ' && unzip ' + file_name + ' && rm ' + file_name
    print(cmd)
    pyperclip.copy(cmd)
else:
    curl = 'curl https://tmpfiles.org/api/v1/upload -F "file=@/"';
    print(curl)
    pyperclip.copy(curl)