import InGame


import json

mapFile = open("Assets/Example.json")

json.load(mapFile)

InGame.Run()