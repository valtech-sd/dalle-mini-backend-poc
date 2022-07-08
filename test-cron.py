
from pip._vendor import requests, urllib3


t = requests.get('https://dalle-mini-ui-seven.vercel.app/api/text-prompt')
j = t.json()
prompt = j['currentPrompt']
r = requests.post('http://127.0.0.1:8080/dalle', json={'num_images': 1, 'text': prompt})

print(r.text)
