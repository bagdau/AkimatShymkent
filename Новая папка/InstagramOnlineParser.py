import requests
import json

access_token = ''
post_id = ''
url = f'https://graph.instagram.com/{post_id}/comments?access_token={access_token}'

response = requests.get(url)
data = response.json()

for comment in data['data']:
    print(comment['text'])