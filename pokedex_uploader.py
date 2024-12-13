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
# function to add the first 151 pokemon (Bulbasaur-Mew) to pokedex.txt
    for x in range(1, 152):
        # loop iterates through the first entries
        pokedex_entry(x)
        # function is called in each iteration to enter 

def pokedex_entry(pkdx_no):
    """
    Function for writing the data in each pokemon as a json dictionary to pokedex.txt 
    """
    pokemon = get_pokemon(pkdx_no)
    # pokemon object declared
    pokemon_info = {"pkdx_no" : pokemon.pkdx_no,
        "name" : pokemon.name,
        "type" : pokemon.type,
        "weight" : pokemon.weight,
        "height" : pokemon.height,
        "front_url" : pokemon.front_url,}
        # formats the data as a json dictionary.
    with open("pokedex.txt", "a") as convert_file:
        # with is used so the file is automatically opened and closed, pokedex.txt is appended to, as declared by "a"
        convert_file.write(json.dumps(pokemon_info)+"\n")
        # write new information on a new line in pokedex.txt

class Pokemon:
    # pokemon class declared to hold data about each pokemon 
    def __init__(self, pkdx_no, name, type, weight, height, front_url):
        self.pkdx_no = pkdx_no
        self.name = name        
        self.type = type
        self.weight = weight
        self.height = height
        self.front_url = front_url 
        # declared different variable for storage and access

def get_pokemon(pkdx_no):
# function for calling data from pokeapi and saving it as a pokemon class object
    url = "https://pokeapi.co/api/v2/pokemon/" + str(pkdx_no)
    # creates an url for calling pokeapi by combing the base url with a number object
    # ex. https://pokeapi.co/api/v2/pokemon/99, Kingler
    response = requests.get(url)
    # queries pokeapi.co for the data on the pokemon
    response = json.loads(response.text)
    # uses json to load the data in the response
    name = response["name"]
    type = response["types"][0]["type"]["name"]
    weight = response["weight"]
    height = response["height"]*10
    front_url = response["sprites"]["front_default"]  
    # variables declared to contain data from pokeapi, in the form of dictionary calls.
    pokemon = Pokemon(pkdx_no, name, type, weight, height, front_url)
    # a pokemon object is created from all the gathered data
    return pokemon
    # the function ends and returns the pokemon class object created above
main()