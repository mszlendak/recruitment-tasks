import requests

from itertools import chain

url = 'https://dog.ceo/api/breeds/list/all'

resp = requests.get(url)
data = resp.json()['message']

uniqueWords = set(chain(data.keys(), chain.from_iterable(data.values())))

log = ["{:5}{:>20}".format(str(k+1) + '.', v) for
       k,v in enumerate(sorted(uniqueWords))]

print("\n".join(log))


