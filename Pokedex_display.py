"""
- [ ] **Regular Expressions**
	*Basic* - Partial Evidence shown, limited depth in the usage of regex
	*Complete* - Full Evidence shown of regex with different filters and functions used
 - [ ] **Testing**
	*Complete* - All functions that can be tested are tested, with individualised tests with a reasonable number
    of test conditions
 - [ ] **Libraries**
	*Complete* - Full Evidence shown, including your own library made
 - [ ] **File I/O**
	*Complete* - Full Evidence shown of reading and writing to .txt or .csv files
 - [ ] **Object Orientated Programming**
	*Basic* - Partial Evidence shown, potentially missing more than one class or inheritance from a super class. 
	*Complete* - Full Evidence shown of classes and inheritance.
 - [ ] **Above and beyond**
	An opportunity for you to expand on the taught content and show extra knowledge, evidencing python outside of
    the categories taught will warrant these extension marks.
    """

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

from urllib.request import urlopen
"""
import requests, json
import pokedex_uploader
import tkinter as tk
from PIL import ImageTk
# call data from pokedex.txt
def main():
    pkdx_data = conversion_module()
    print(pkdx_data[0])

def pokedex_cell(pkdx_no):
    # function to render one pokedex widget. in the form:
    # pkdx_no, name
    # fronturl. 
    print(pokedex_length())

    ...
def pokedex_length():
    pkdx_data = conversion_module()
    pkdx_length = len(pkdx_data)
    return pkdx_length
def conversion_module():
    with open('pokedex.txt', 'r') as file:
        data = file.read()    
    pkdx_data = data.split("\n")
    
    return pkdx_data

# initial step, define creation of a widget and grid for display of those widgets
main()