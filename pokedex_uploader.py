import tkinter as tk 
import requests, json
def main():
    pokemon = get_pokemon(1)
    print(f"{pokemon.name}")

def first_gen_upload():
    ...
def pokedex_entry(pkdx_no):
    ...

class Pokemon:
    def __init__(self, name, number, type, weight, height, front_url, stats):
        self.name = name
        self.number = number
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
    weight = response["weight"]
    height = response["height"]*10
    front_url = response["sprites"]["front_default"]
    stats = response["stats"]
    response["name"]
    pokemon = Pokemon(number, name, weight, height, front_url, stats)
    return pokemon


if __name__ == "__main__":
    main()