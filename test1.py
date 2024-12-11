import requests, json
url = "https://pokeapi.co/api/v2/pokemon-form/"
for x in range(150, 152):
    number = str(x)
    response = requests.get(url + number)
    response = json.loads(response.text)
    print(response["name"])

