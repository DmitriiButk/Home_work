import requests

# Задание 1
url = "https://akabab.github.io/superhero-api/api/all.json"
response = requests.get(url)
hero_list = ['Hulk', 'Captain America', 'Thanos']
powerstats = {}
for hero in hero_list:
    for hero2 in response.json():
        if hero2['name'] == hero:
            powerstats.update({hero: hero2['powerstats']['intelligence']})
print(f'Самый умный супергерой: {[key for key, value in powerstats.items() if value == max(powerstats.values())][0]}')

# Задание 2
class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, path_to_file):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        for file in path_to_file:
            url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
            params = {
                'path': file
            }
            headers = {
                'Authorization': token
            }
            res = requests.get(url, params=params, headers=headers)
            url_for_upload = res.json().get('href', '')
            with open(file, 'rb') as f:
                requests.put(url_for_upload, files={'file': f})

file_list = ['1.jpg', '2.jpg', '3.jpg']

if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = file_list
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)