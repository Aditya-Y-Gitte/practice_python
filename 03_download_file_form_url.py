import requests
url = ''


response = requests.get(url)
file_Path = ''

if response.status_code == 200:
    with open(file_Path, 'wb') as file:
        file.write(response.content)
    print('File downloaded successfully')
else:
    print('Failed to download file')

print(dir(requests))