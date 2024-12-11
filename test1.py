from urllib.request import urlopen
import requests, json
from PIL import ImageTk
"""
url = "https://pokeapi.co/api/v2/pokemon-form/"
for x in range(150, 152):
    number = str(x)
    response = requests.get(url + number)
    response = json.loads(response.text)
    print(response["name"])
"""
"""import tkinter as tk 
url = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/500.png"
number = "1"
window = tk.Tk()

data = urlopen(url)
image = ImageTk.PhotoImage(data=data.read())
tk.Label(window, image=image).pack()

window.mainloop()
"""
"""
url = "https://pokeapi.co/api/v2/pokemon/1"
response = requests.get(url)
response = json.loads(response.text)
response["name"]
response["weight"]
response["height"]*10
response["stats"]
response["sprites"]["front_default"]
"""
def main():
    """
    pokemon = get_pokemon(809)
    print(f"{pokemon.stats}")
    """
    first_gen_entry()

def first_gen_entry():

    for x in range(1, 152):
        pokedex_entry(x)

def pokedex_entry(pkdx_no):
    pokemon = get_pokemon(pkdx_no)
    pokemon_info = {"pkdx_no" : pokemon.number,
        "name" : pokemon.name,
        "type" : pokemon.type,
        "weight" : pokemon.weight,
        "height" : pokemon.height,
        "front_url" : pokemon.front_url,
        "stats" : pokemon.stats,}
    print(pokemon_info)
    with open("pokedex_test.txt", "a") as convert_file:
        # with is used so the file is automatically opened and closed, pokedex.txt
        convert_file.write(json.dumps(pokemon_info)+"\n")

class Pokemon:
    def __init__(self, number, name, type, weight, height, front_url, stats):
        self.number = number
        self.name = name        
        self.type = type
        self.weight = weight
        self.height = height
        self.front_url = front_url 
        self.stats = stats

def get_pokemon(pkdx_no):
    url = "https://pokeapi.co/api/v2/pokemon/" + str(pkdx_no)
    response = requests.get(url)
    response = json.loads(response.text)
    name = response["name"]
    number = pkdx_no
    type = response["types"][0]["type"]["name"]
    weight = response["weight"]
    height = response["height"]*10
    front_url = response["sprites"]["front_default"]
    stats = response["stats"]
    response["name"]
    pokemon = Pokemon(number, name, type, weight, height, front_url, stats)
    return pokemon
main()