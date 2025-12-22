import sys
import json
import requests


url = "https://itunes.apple.com/search?entity=song&limit=50&term="
if len(sys.argv) != 2:
    sys.exit()

response = requests.get(url + sys.argv[1])
# print(json.dumps(response.json(), indent= 2))

songs = response.json()

for i, song in enumerate(songs["results"]):
    print(f"{i+1}. {song["trackName"]}")

