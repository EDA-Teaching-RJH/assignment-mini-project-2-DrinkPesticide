import requests, json
pkdx_no = 88
url = "https://pokeapi.co/api/v2/pokemon/" + str(pkdx_no)
response = requests.get(url)
response = json.loads(response.text)
print(response["types"][0]["type"]["name"])