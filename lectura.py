import json
from pprint import pprint
with open(r"2011light.json") as f:
	datos=json.load(f)
print("se va a leer: \n orchestra\n del primer\n programs\n asi: datos[programs][0][orchesta] omitiendo comillas\n")
resultado=datos["programs"][0]["orchestra"]
print(resultado+"\n")
input("Salir?")