import json
import os

import requests
from bs4 import BeautifulSoup

print('[*] Connecting to blush.design...')
response = requests.get(
    'https://blush.design/collections/rChdrB8vX8xQJunpDPp8/avatars/avataaar-default/')

if response.status_code == 200:
    print('[+] Connection successful. Parsing page...')
    soup = BeautifulSoup(response.text, features='lxml')
    avatar_parts = soup.find("script", {"id": "__NEXT_DATA__"})
    print('[+] Avatar parts retrieved. Parsing avatar parts...')
    parsed_json = json.loads(avatar_parts.contents[0])
    avatar_parts = parsed_json['props']['pageProps']['initialBlushData']['modificationOptions']['children']
    print(f'[+] {len(avatar_parts)} attributes found')
    for attr in avatar_parts:
        print(f'        * {attr["id"]}')

    print('[*] Starting downloads...')
    for elem in avatar_parts:
        id_path = f'downloads/{elem["id"]}'
        os.makedirs(id_path)
        for option in elem['options']:

            print(f'[*] Downloading {elem["id"]}/{option}...')

            url = f'https://cdn.blush.design/collections/rChdrB8vX8xQJunpDPp8/v16/{elem["id"]}/cropped/{option}.svg'
            response = requests.get(url)

            if response.status_code == 200:
                option = option.replace(' ', '_')
                option = option.lower()

                with open(f'{id_path}/{option}.svg', 'w', encoding='utf-8') as f:
                    f.write(response.text)
            else:
                print(
                    f'[!] {elem["id"]}/{option}... download error: {response.status_code}')
    print('[+] Finished!')
else:
    print(f'[!] Connection error: {response.status_code}')
