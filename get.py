import requests
import json

response = requests.get(
    'https://api.stackexchange.com/2.3/questions?order=desc&sort=votes&site=stackoverflow')

title = []
link = []
for data in response.json()['items']:
    if data['answer_count'] == 0:
        title.apppend(data['title'])
        link.append(data['link'])
    else:
        print('skip this line')
        continue
