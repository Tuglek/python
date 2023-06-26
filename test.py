import requests

TOKEN = '6245274012:AAHzbKrd0OVSOiE1pgIte-nfeR3UdgeY28M'
url = f'https://api.telegram.org/bot{TOKEN}/getUpdates'

response =requests.get(url)
print(response.json())