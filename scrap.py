import requests
from bs4 import BeautifulSoup
import json

url = 'https://www.instagram.com/wearelikewise/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

script = soup.findAll('script', {'type': 'text/javascript'})[3]
raw_data = script.replace(';', '').replace('window._sharedData = ', '')
json_data = json.loads(raw_data)

user_data = json_data['entry_data']['ProfilePage'][0]['graphql']['user']

posts = user_data['edge_owner_to_timeline_media']['edges']

total_likes = 0

for post in posts:
    total_likes += post['node']['edge_liked_by']['count']

print(total_likes/len(posts))

# try to use get_text() instead of .text

