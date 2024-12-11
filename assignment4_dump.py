import requests
import json
def get_weather(city, api_key):
    """
The function is declared in order to:
(1.) Take the city location and api_key from main in dinosaur.
(2.) compile those details with the pre written content in response with input variables. 
e.g: https://api.openweathermap.org/data/2.5/weather?q=canterbury&appid=
"""
    base_url = "https://api.openweathermap.org/data/2.5/weather?"   
    response = requests.get(base_url + "q=" + city + "&appid=" + api_key) 
    # assembling response. e.g: https://api.openweathermap.org/data/2.5/weather?q=canterbury&appid=
    #if response.status_code == 200:
        # returns response as an int from the weather dict.
    response = json.loads(response.text)
        # compiles text into an accessible format
    return response
    #else:
       # return {"cod":404, "message":"city not found"}
        # failure branch, structure in this odd way because i couldn't figure out how to get it to behave
        # nevermind ; )
        # error handling moved to dinosaur.py

"""
For this assignment you are required to create an ASCII Dinosaur which tells the current weather dependant on a command line argument. Some boiler plate code is provided with an API Key for a weather service. 

You must have: 
(1.)[Complete] A command line argument which determines the location of the weather request.(10 Marks)
(2.)[Complete] Usage of two python files. weatherQuery.py has been semi-populated for you, 
while you need to write all of dinosaur.py. Your cowsay element should be in dinosaur.py.(70 Marks)
(3.)[Complete] A dinosaur which gives the string output of the current weather (using the cowsay library). (10 Marks)
(4.)[] Comments detailing your code (10 Marks)
"""
import cowsay, sys
from weatherQuery import get_weather
dimetrodon = r"""
\
 \                        _._
  \                     _/:|:
                       /||||||.
                       ||||||||.
                      /|||||||||:
                     /|||||||||||
                    .|||||||||||||
                    | ||||||||||||:
                  _/| |||||||||||||:_=---.._
                  | | |||||:'''':||  '~-._  '-.
                _/| | ||'         '-._   _:    ;
                | | | '               '~~     _;
                | '                _.=._    _-~
             _.~                  {     '-_'
     _.--=.-~       _.._          {_       }
 _.-~   @-,        {    '-._     _. '~==+  |
('          }       \_      \_.=~       |  |
`======='  /_         ~-_    )         <_oo_>
  `-----~~/ /'===...===' +   /
         <_oo_>         /  //
                       /  // 
                      <_oo_>
"""
# dimetrodon given in docstring format.
# please forgive the dimetrodon for being a non-mammalian synapsid.
def main():
  """
  this file needs to be run alongside an argument for location
  testing was done in powershell. e.g: python dinosaur.py faversham
  variables:
    output(str): 
    - temperature(float), humidity(int), description(string), output(str)
  """
  if len(sys.argv) == 2:
    # filename is argument 0, cityname is argument 1, so the correct branch is when sys.argv = 2 
    response = get_weather(sys.argv[1], "f3d6d1f6c418203d3d2c727199918c83")
    status_code = response["cod"]
    if status_code == 404:
      print(cowsay.draw(response["message"], dimetrodon))
      # error branch. cowsay, declared above is used to print my custom 'dinosaur'.
    elif status_code == 200:
      temperature = round(((response["main"]["temp"])-273.15), 2)
      # temp converted to kelvin with a simple subtraction
      humidity = response["main"]["humidity"]
      description = response["weather"][0]["description"]      
      # variable declarations above are used to assemble the output
      output = f"Weather in {sys.argv[1]}:\nTemperature: {temperature}°C\nHumidity: {humidity}%\nDescription: {description}"
      # output is compiled into an f string to mimic the brief
      print(cowsay.draw(output, dimetrodon))
  elif len(sys.argv) < 2:
    print(cowsay.draw("No location argument entered!", dimetrodon))
    # in this case too few arguments are entered. e.g: python dinosaur.py 
  elif len(sys.argv) > 2:
    print(cowsay.draw("Too many arguments entered!", dimetrodon))
    # in this case too many arguments are entered. e.g: python dinosaur.py faversham canterbury london
main()