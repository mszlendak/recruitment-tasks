import requests
import json

url = 'https://dog.ceo/api/breeds/list/all'

resp = requests.get(url)
data = json.loads(resp.text)['message']

words = []

for k, v in data.items():
    words.append(k)

    for vv in data[k]:
        words.append(vv)

words.sort()
uniqueWords = []

for word in words:
    if word not in uniqueWords:
        uniqueWords.append(word)

lp = 1
log = []

for k, v in enumerate(uniqueWords):
    log.append('%-5s%20s' % (str(lp) + '.', v))
    lp += 1

print("\n".join(log))
