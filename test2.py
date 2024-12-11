import requests, json
pkdx_no = 88
url = "https://pokeapi.co/api/v2/pokemon/" + str(pkdx_no)
response = requests.get(url)
response = json.loads(response.text)
print(response["types"][0]["type"]["name"])
upload = response["types"][0]

with open("pokedex_test.txt", "w") as pokedex_test_file:
    # with is used so the file is automatically opened and closed, pokedex.txt
    pokedex_test_file.write(upload)