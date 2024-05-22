
import os
import sys
import pyperclip
import requests
from zipfile import ZipFile

if len(sys.argv) > 1:
    file_name = 'temp_files.zip'
    files = sys.argv[1:]

    for i in range(len(files)):
        if files[i].endswith('/') or files[i].endswith('\\'):
            files[i] = files[i][:-1]
            
    with ZipFile(file_name, 'w') as zip:
        for file in files:
            if os.path.isdir(file):
                for root, dirs, files in os.walk(file):
                    for f in files:
                        zip.write(os.path.join(root, f), os.path.relpath(os.path.join(root, f), os.path.join(file, '..')))
            else:
                zip.write(file, os.path.basename(file))
        
    response = requests.request('POST', 'https://tmpfiles.org/api/v1/upload', files={'file': open(file_name, 'rb')})
    os.remove(file_name)
    
    url = response.json()['data']['url'].replace('https://tmpfiles.org/', 'https://tmpfiles.org/dl/')
    cmd = f'curl -o {file_name} {url}' + ' && unzip ' + file_name + ' && rm ' + file_name
    print(cmd)
    pyperclip.copy(cmd)
else:
    curl = 'curl https://tmpfiles.org/api/v1/upload -F "file=@/"';
    print(curl)
    pyperclip.copy(curl)